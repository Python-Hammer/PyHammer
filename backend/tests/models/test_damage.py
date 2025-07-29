import pytest

import numpy as np

from models.damage import Damage


RANDOM_SEED = 42


@pytest.fixture(autouse=True)
def set_random_seed():
    """
    Set a random seed for reproducibility in tests.
    """
    np.random.seed(RANDOM_SEED)


@pytest.mark.parametrize(
    "damage_profile,samples,add_modifier,expected_result",
    [
        ("1d3+1", 3, -2, 4),
        ("2d6", 1, 3, 12),
        (4, 2, 1, 10),
    ],
)
def test_damage_value(damage_profile, samples, add_modifier, expected_result):
    damage_class = Damage(damage_profile)
    damage_output = damage_class.damage_value(samples=samples, add_modifier=add_modifier)
    assert damage_output == expected_result, f"Expected {expected_result}, got {damage_output}"
