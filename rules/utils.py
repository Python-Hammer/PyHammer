from numpy.random import randint
import numpy as np


def roll_dice(n_sides: int = 6, samples: int = 1) -> np.ndarray:
    """
    Rolls samples times a n_sides sided dice. Returns the result as a numpy array.
    """
    return randint(1, n_sides + 1, samples)


def roll_test(value, dice, samples, return_crits=False):
    # TODO: return type changes depending on parameters!! to fix
    if return_crits:
        rolls = roll_dice(6, samples)
        return rolls >= value, rolls == 6
    return roll_dice(dice, samples) >= value


def bound_target_value(x: int) -> int:
    """
    Binds the target value of a d6 roll between 2 and 7.
    1+ tests do not exist, and 7+ tests are always a fail.
    """
    return max(2, min(x, 7))


def bound_save_target_value(x: int, x_old: int) -> int:
    """
    Binds the target value of a save.
    A save difficulty cannot be lower than its original value - 1.
    """
    # TODO: generalize that function to hit and wound rolls?
    # hit and wound cant be easier than original value - 1
    # but they also cant be harder than original value + 1
    x_bound = bound_target_value(x)
    return np.maximum(x_old - 1, x_bound)


def roll_d3_above_2(samples: int = 1) -> np.ndarray:
    """
    Rolls a d3 and returns 0 if the result is 1
    """
    roll = roll_dice(3, samples)
    return np.where(roll == 1, 0, roll)
