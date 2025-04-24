from numpy.random import randint
import numpy as np


def D(n, samples=1):
    return randint(1, n + 1, samples)


def roll_test(value, dice, samples, return_crits=False):
    # TODO: return type changes depending on parameters!! to fix
    if return_crits:
        rolls = D(6, samples)
        return rolls >= value, rolls == 6
    return D(dice, samples) >= value


def bound_target_value(x: int) -> int:
    """
    Binds the target value of a d6 roll between 2 and 7.
    1+ tests do not exist, and 7+ tests are always a fail.
    """
    return max(2, min(x, 7))


def bound_save_target_value(x, x_old):
    """
    Binds the target value of a save.
    A save difficulty cannot be lower than its original value - 1.
    """
    # TODO: generalize that function to hit and wound rolls?
    # hit and wound cant be easier than original value - 1
    # but they also cant be harder than original value + 1
    x_bound = bound_target_value(x)
    return np.maximum(x_old - 1, x_bound)


def miniD3(samples):
    roll = D(3, samples)
    roll = np.where(roll == 1, 0, roll)
    return roll
