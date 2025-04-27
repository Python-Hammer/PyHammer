import pytest

from models.damage import Damage
from models.weapon import Weapon


@pytest.fixture(scope="function", autouse=True)
def set_random_seed():
    """
    Set a random seed for reproducibility in tests.
    """
    import numpy as np

    np.random.seed(42)


@pytest.fixture(scope="module")
def setup_weapon():
    """
    Fixture to set up a weapon instance for testing.
    """
    weapon_data = {
        "attacks": 2,
        "to_hit": 3,
        "to_wound": 4,
        "rend": 1,
        "damage": "1d3+1",
        "special_rules": [
            {"id": "add_to_hit", "condition": "cavalry", "value": 1},
            {"id": "add_rend", "condition": "charged", "value": 2},
            {"id": "crit_mortal"},
        ],
    }
    weapon = Weapon(weapon_data)
    return weapon


def test_weapon_initialization():
    weapon = Weapon(
        {
            "attacks": 2,
            "to_hit": 3,
            "to_wound": 4,
            "rend": -1,
            "damage": "1d6",
            "special_rules": [{"id": "add_to_hit", "condition": "charged", "value": 1}],
        }
    )
    assert weapon.attacks == 2
    assert weapon.to_hit == 3
    assert weapon.to_wound == 4
    assert weapon.rend == -1
    assert weapon.damage.num_dice == 1
    assert weapon.damage.sides == 6
    assert weapon.special_rules == [{"id": "add_to_hit", "condition": "charged", "value": 1}]
    assert isinstance(weapon.damage, Damage)


def test_find_modifier_total_value():
    weapon = Weapon(
        {
            "attacks": 2,
            "to_hit": 3,
            "to_wound": 4,
            "rend": -1,
            "damage": "1d6",
            "special_rules": [
                {"id": "add_to_hit", "condition": "charged", "value": 1},
                {"id": "add_attacks", "condition": "wounded", "value": -1},
            ],
        }
    )
    combat_context = {"charged": False, "add_to_hit": 2, "wounded": True}
    assert weapon._find_modifier_total_value("to_hit", combat_context) == 2
    assert weapon._find_modifier_total_value("attacks", combat_context) == -1


def test_process_hit_rolls(setup_weapon):
    weapon = setup_weapon
    combat_context = {"cavalry": True, "charged": False}
    results = weapon._process_hit_rolls(30, combat_context)
    assert results["hits"] == 27, "Expected 27 hits, got {}".format(results["hits"])
    assert results["wounds"] == 0, "Expected 0 wounds, got {}".format(results["wounds"])
    assert results["mortals"] == 4, "Expected 4 mortals, got {}".format(results["mortals"])


@pytest.mark.parametrize(
    "special_rules,context,expected_wounds",
    [
        (
            [{"id": "add_to_wound", "value": -2, "condition": "infantry"}],
            {"infantry": True},
            11,
        ),  # -1 wound from rules
        ([{"id": "crit_2_hits"}], {}, 17),  # Extra hit on 6s, no effect here
        ([], {"add_to_wound": 1}, 23),  # +1 to wound from context
        ([], {"add_to_wound": 2}, 23),  # +2 to wound from context, equivalent to +1
    ],
)
def test_process_wound_rolls(setup_weapon, special_rules, context, expected_wounds):
    weapon = setup_weapon
    weapon.special_rules = special_rules
    results = weapon._process_wound_rolls(30, context)
    assert results["wounds"] == expected_wounds, "Expected {} wounds, got {}".format(
        expected_wounds, results["wounds"]
    )


@pytest.mark.parametrize(
    "special_rules,context,save,expected_damage",
    [
        ([], {}, 3, 13),  # 4+ effective save, 30 hits 1 rend
        ([{"id": "add_rend", "condition": "charged", "value": 2}], {"charged": True}, 3, 26),
        (
            [{"id": "add_rend", "condition": "infantry", "value": 2}],
            {"add_save": 2},
            5,
            13,
        ),  # 4+ effective save
        ([{"id": "add_rend", "condition": "infantry", "value": 2}], {}, 4, 19),  # 5+ effective save
        ([], {"charged": True}, 6, 30),  # all hits go through, save is 7 with 1 rend
    ],
)
def test_save_rolls(setup_weapon, special_rules, context, save, expected_damage):
    """
    Tests save rolls for 30 succeeded wounds.
    """
    weapon = setup_weapon
    weapon.special_rules = special_rules
    results = weapon._process_save_rolls(30, save, context)
    assert results["successful_attacks"] == expected_damage, "Expected {} successful attacks, got {}".format(
        expected_damage, results["successful_attacks"]
    )


@pytest.mark.parametrize(
    "damage, context, expected_damage",
    [
        (14, {}, 14),  # No ward, full damage
        (30, {"ward": 2}, 3),  # 2+ ward, low damage
        (199, {"ward": 7}, 199),  # 7+ ward, full damage
        (30, {"ward": 1}, 3),  # 1+ ward, equivalent to 2+
    ],
)
def test_ward_rolls(setup_weapon, damage, context, expected_damage):
    final_damage = setup_weapon._process_ward_rolls(damage, context)["final_damage"]
    assert final_damage == expected_damage, "Expected {} final damage, got {}".format(
        expected_damage, final_damage
    )


@pytest.mark.parametrize(
    "weapon_data,attack_count,enemy_save,context,expected_damage",
    [
        # Basic attack without special rules
        (
            {
                "attacks": 2,
                "to_hit": 4,
                "to_wound": 4,
                "rend": 0,
                "damage": 2,
            },
            30,  # 30 attacks (15 models)
            5,  # 5+ save
            {},  # No special context
            14,  # Expected damage with random seed 42
        ),
        # Attack with critical effects
        (
            {
                "attacks": 2,
                "to_hit": 4,
                "to_wound": 4,
                "rend": 0,
                "damage": 2,
                "special_rules": [{"id": "crit_mortal"}],
            },
            30,  # 30 attacks
            5,  # 5+ save
            {},  # No special context
            22,  # Expected damage with random seed 42 (includes mortal wounds)
        ),
        # Attack with conditional modifiers
        (
            {
                "attacks": 2,
                "to_hit": 4,
                "to_wound": 4,
                "rend": 0,
                "damage": 2,
                "special_rules": [{"id": "add_rend", "condition": "charged", "value": 1}],
            },
            30,  # 30 attacks
            5,  # 5+ save
            {"charged": True},  # Charged context activates rend
            16,  # Expected damage with random seed 42 (increased due to rend)
        ),
        # Attack against target with ward save
        (
            {
                "attacks": 2,
                "to_hit": 4,
                "to_wound": 4,
                "rend": 0,
                "damage": 2,
                "special_rules": [{"id": "add_rend", "condition": "charged", "value": 1}],
            },
            30,  # 30 attacks
            5,  # 5+ save
            {"ward": 5, "charged": True},  # Charged context activates rend
            11,  # Expected damage with random seed 42 (reduced due to ward save)
        ),
    ],
)
def test_resolve_attacks(weapon_data, attack_count, enemy_save, context, expected_damage):
    """Test full attack resolution with various weapon profiles and contexts"""
    weapon = Weapon(weapon_data)
    damage = weapon.resolve_attacks(attack_count, enemy_save, context)

    assert damage == expected_damage, f"Expected {expected_damage} damage but got {damage}"
