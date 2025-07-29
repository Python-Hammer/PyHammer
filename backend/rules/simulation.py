from models.profile import Profile


def simulate_combat(
    attacker: Profile,
    defender: Profile,
    attacker_context_dict: dict = None,
    defender_context_dict: dict = None,
) -> dict:
    """
    Simulate a combat between two profiles.
    The attacker and defender are instances of the Profile class.
    The combat_context_dict can include additional information like situational buffs,
    debuffs, mortal damage on top of the fight, etc.
    The attacker_context_dict (respectively defender) includes everything relevant to their attacks and saves
    (be it buffs from the attacker or debuffs from the defender).
    """

    attacker_damage = attacker.attack_with_all_weapons(attacker_context_dict, defender.save)
    defender_models_slain, attacker_damage = defender.receive_damage(attacker_damage)

    defender_damage = defender.attack_with_all_weapons(defender_context_dict, attacker.save)
    attacker_models_slain, defender_damage = attacker.receive_damage(defender_damage)

    return {
        "attacker": {
            "models_slain": attacker_models_slain,
            "remaining_models": attacker.current_models,
            "damage_received": defender_damage,
        },
        "defender": {
            "models_slain": defender_models_slain,
            "remaining_models": defender.current_models,
            "damage_received": attacker_damage,
        },
    }
