from models.weapon import Weapon


class Profile:
    def __init__(self, unit_data: dict, is_reinforced: bool = False):
        self.name = unit_data["name"]
        self.cost = unit_data["point_cost"]
        self.total_models = unit_data["model_count"] if not is_reinforced else 2 * unit_data["model_count"]
        self.current_models = unit_data["model_count"] if not is_reinforced else 2 * unit_data["model_count"]
        self.health = unit_data["health"]
        self.save = unit_data["save"]
        self.ward = unit_data.get("ward", None)
        self.champion = unit_data.get("has_champion", True)

        # Initialize weapons
        self.weapons: list[Weapon] = []
        for weapon_data in unit_data.get("weapons", []):
            weapon = Weapon(weapon_data)
            self.weapons.append(weapon)

    def attack_with_all_weapons(self, combat_context: dict, enemy_save: int) -> int:
        """Perform attacks with all weapons and return the resulting damage."""
        all_results = []
        for weapon in self.weapons:
            nb_attacks = weapon.attacks * self.current_models
            if self.champion and "companion" not in [rule["id"] for rule in weapon.special_rules]:
                nb_attacks += 1
            results = weapon.resolve_attacks(nb_attacks, enemy_save, combat_context)
            all_results.append(results)
        return sum(all_results)
