from models.damage import Damage
from rules.utils import (
    bound_target_value,
    bound_hit_wound_target_value,
    bound_save_target_value,
    roll_test,
    roll_test_with_crit,
)


class Weapon:
    """
    Class representing a weapon in the game.
    Contains every information about the weapon, including its stats and special rules.
    This class handles the main attack resolution process.
    It is used by the Profile class to resolve attacks.
    """

    def __init__(self, weapon_data: dict):
        self.attacks = weapon_data["attacks"]
        self.to_hit = weapon_data["to_hit"]
        self.to_wound = weapon_data["to_wound"]
        self.rend = weapon_data.get("rend", 0)
        self.damage = Damage(weapon_data["damage"])
        self.special_rules = weapon_data.get("special_rules", [])

    def _find_modifier_total_value(self, value_name: int, combat_context: dict) -> int:
        """
        Changes a value depending on both the weapon's special rules and the combat context.
        Returns a relative integer value, without bounds (rules limiting modifiers to +1 or -1).
        """
        value = 0
        weapon_is_companion = any(rule["id"] == "companion" for rule in self.special_rules)
        if not weapon_is_companion:
            for rule in self.special_rules:
                if rule["id"] == f"add_{value_name}" and combat_context.get(rule["condition"]):
                    value += rule["value"]
            value += combat_context.get("add_" + value_name, 0)
        else:
            for rule in self.special_rules:
                if rule["id"] == f"add_{value_name}_companion" and combat_context.get(rule["condition"]):
                    value += rule["value"]
            value += combat_context.get("add_" + value_name + "_companion", 0)

        return value

    def _process_hit_rolls(self, attacks: int, combat_context: dict) -> dict:
        """
        Process the hit rolls based on the weapon's special rules.
        """
        attacks = max(attacks, 1)
        results = {"hits": 0, "wounds": 0, "mortals": 0}
        crit_auto_wound = any(rule["id"] == "auto_wound" for rule in self.special_rules)
        crit_mortal = any(rule["id"] == "crit_mortal" for rule in self.special_rules)
        crit_2_hits = any(rule["id"] == "crit_2_hits" for rule in self.special_rules)
        to_hit_mod = self._find_modifier_total_value("to_hit", combat_context)
        to_hit = bound_hit_wound_target_value(self.to_hit, -to_hit_mod)  # Negative modifier
        # because applied to the target value

        if any([crit_auto_wound, crit_mortal, crit_2_hits]):
            hit_rolls, crit_rolls = roll_test_with_crit(to_hit, attacks)
            results["hits"] = hit_rolls.sum()
            if crit_auto_wound:
                results["wounds"] += crit_rolls.sum()
            if crit_mortal:
                results["mortals"] += crit_rolls.sum()
            if crit_2_hits:
                results["hits"] += crit_rolls.sum()
        else:
            hit_rolls = roll_test(to_hit, attacks)
            results["hits"] = hit_rolls.sum()

        return results

    def _process_wound_rolls(self, hits: int, combat_context: dict) -> dict:
        """
        Process the wound rolls based on the weapon's special rules.
        """
        results = {"wounds": 0}
        to_wound_mod = self._find_modifier_total_value("to_wound", combat_context)
        to_wound = bound_hit_wound_target_value(self.to_wound, -to_wound_mod)
        # Negative modifier because applied to the target value
        results["wounds"] = roll_test(to_wound, hits).sum()

        return results

    def _process_save_rolls(self, wounds: int, enemy_save: int, combat_context: dict) -> dict:
        """
        Processes the save rolls based on the weapon's special rules and
        taking into account the rend of the weapon.
        Any attack where the save roll succeeds is a failed attack.
        Any other attack is a successful attack.
        """
        results = {"successful_attacks": 0}
        save_mod = self._find_modifier_total_value("save", combat_context)
        rend = max(self.rend + self._find_modifier_total_value("rend", combat_context), 0)
        save_mod = save_mod - rend
        save = bound_save_target_value(enemy_save, -save_mod)
        # Negative modifier because applied to the target value
        results["successful_attacks"] = wounds - roll_test(save, wounds).sum()

        return results

    def _process_ward_rolls(self, total_damage: int, combat_context: dict) -> dict:
        """
        Processes the ward rolls based on the weapon's special rules and
        taking into account the enemy's ward save.
        Any damage that goes through the ward removes health from the target.
        Any succeeded ward roll nullifies one damage.
        """
        enemy_ward = bound_target_value(combat_context.get("ward", 7))
        ward_mod = self._find_modifier_total_value("ward", {})
        enemy_ward = enemy_ward - ward_mod  # edge case that happens for some rare abilities
        results = {"final_damage": total_damage}
        results["final_damage"] -= roll_test(enemy_ward, total_damage).sum()
        return results

    def resolve_attacks(self, attack_count: int, enemy_save: int, combat_context: list = None):
        """
        Attacks with the weapon against a target with a given save.
        The combat_context can include additional information like rerolls, modifiers, etc.
        from either the attacker or the defender.
        """
        if combat_context is None:
            combat_context = []

        hit_rolls = self._process_hit_rolls(attack_count, combat_context)
        wound_rolls = self._process_wound_rolls(hit_rolls["hits"], combat_context)
        save_rolls = self._process_save_rolls(wound_rolls["wounds"], enemy_save, combat_context)
        damage_mod = self._find_modifier_total_value("damage", combat_context)
        total_damage = self.damage.damage_value(
            samples=save_rolls["successful_attacks"] + hit_rolls["mortals"], add_modifier=damage_mod
        )
        total_damage = self._process_ward_rolls(total_damage, combat_context)["final_damage"]

        return total_damage
