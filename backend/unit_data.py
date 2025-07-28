# Example unit data
units = {
    "Steam Tank": {"attack": 50, "defense": 30},
    "Immortis Guard": {"attack": 40, "defense": 20},
}

def get_unit_stats(name):
    return units.get(name)
