'''
Example:

"abilities": [
                {
                    "name": "Deathly Furrows",
                    "id": "impact_mortals",
                    "damage": 1,
                    "roll": "3+"
                }

'''
from rules.utils import roll_test

def impact_mortals(current_models:int, ability_data: dict, combat_context: dict) -> int:
    """
    Resolve the impact mortals ability.
    
    Args:
        ability_data (dict): Data for the impact mortals ability.
        combat_context (dict): Context for the combat.
    Returns:
        int: The number of mortal wounds inflicted.
    """
    damage = ability_data.get('damage', 0)
    test_value = ability_data.get('roll', '3+')
    # Extract the target value from the roll string (e.g., "3+" -> 3)
    test_value = int(test_value[:-1]) if test_value.endswith('+') else int(test_value)
    mortals = 0
    for _ in range(current_models):
        # Roll a d6 and check if it meets the test value
        if roll_test(test_value, 1)[0]:
            mortals += damage
    return mortals