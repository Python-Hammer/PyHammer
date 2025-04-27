from numpy.random import randint
import numpy as np
import numpy.typing as npt


def roll_dice(n_sides: int = 6, samples: int = 1) -> npt.ArrayLike:
    """
    Rolls samples times a n_sides sided dice. Returns the result as a numpy array.
    """
    return randint(1, n_sides + 1, samples)


def roll_test(value: int, samples: int) -> npt.ArrayLike:
    return roll_dice(n_sides=6, samples=samples) >= value


def roll_test_with_crit(
    value: int, samples: int, crit_threshold: int = 6
) -> tuple[npt.ArrayLike, npt.ArrayLike]:
    """
    Rolls samples times a d6 and returns True if the roll is greater than or equal to value.
    If the roll is above crit_threshold (e.g. Power of Hysh), it returns True.
    """
    rolls = roll_dice(n_sides=6, samples=samples)
    return rolls >= value, rolls >= crit_threshold


def bound_target_value(x: int) -> int:
    """
    Binds the target value of a d6 roll between 2 and 7.
    1+ tests do not exist, and 7+ tests are always a fail.
    """
    return np.maximum(2, np.minimum(x, 7))


def bound_hit_wound_target_value(original_value: int, modifier: int) -> int:
    """
    Binds the target value of a hit or wound roll.
    A hit or wound cannot be lower than 2 or higher than 7,
    and cannot be lower than the original value - 1 or
    higher than the original value + 1.
    """
    modified_value = original_value + modifier
    min_allowed = np.maximum(original_value - 1, 2)
    max_allowed = np.minimum(original_value + 1, 7)
    return np.maximum(min_allowed, np.minimum(modified_value, max_allowed))


def bound_save_target_value(original_value: int, modifier: int) -> int:
    """
    Binds the target value of a save.
    A save difficulty cannot be lower than its original value - 1.
    """
    modified_value = original_value + modifier
    x_bound = bound_target_value(modified_value)
    return np.maximum(original_value - 1, x_bound)


def roll_d3_above_2(samples: int = 1) -> npt.ArrayLike:
    """
    Rolls a d3 and returns 0 if the result is 1
    """
    roll = roll_dice(3, samples)
    return np.where(roll == 1, 0, roll)
