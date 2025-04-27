from typing import Union

import numpy as np

from rules.utils import roll_dice, parse_roll_expression


class Damage:
    def __init__(self, damage_profile: Union[int, str]):
        if isinstance(damage_profile, int):
            self.damage_type = "fixed"
            self.value = damage_profile
        else:
            self.damage_type = "variable"
            self.expression = parse_roll_expression(damage_profile)
            self.num_dice = self.expression["num_dice"]
            self.sides = self.expression["sides"]
            self.modifier = self.expression["modifier"]

    def damage_value(self, samples: int = 1, add_modifier: int = 0) -> int:
        if self.damage_type == "fixed":
            return np.full(samples, self.value + add_modifier).sum()
        else:
            return (
                roll_dice(self.sides, self.num_dice * samples).sum()
                + (self.modifier + add_modifier) * samples
            )
