def parse_roll_expression(expression: str):
    """
    Parse a roll expression like "2d6+3" into a dict with keys "num_dice", "sides", and "modifier".
    For example, "2d6+3" would return {"num_dice": 2, "sides": 6, "modifier": 3}.
    """
    parts = expression.split("+")
    base = parts[0]
    modifier = int(parts[1]) if len(parts) > 1 else 0

    if "d" in base:
        num_dice, sides = map(int, base.split("d"))
        return {"num_dice": num_dice, "sides": sides, "modifier": modifier}
    else:  # in case a flat value is passed as a string
        return {"num_dice": 0, "sides": 0, "modifier": int(base)}
