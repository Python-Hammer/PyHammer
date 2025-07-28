def calculate_damage(attacker, defender):
    # Simple formula: attack - defense (minimum 0)
    return max(attacker["attack"] - defender["defense"], 0)
