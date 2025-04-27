from models.weapon import Weapon


class Profile:
    def __init__(self, unit_data: dict):
        self.name = unit_data["name"]
        self.cost = unit_data["cost"]
        self.models = unit_data["models"]
        self.health = unit_data["health"]
        self.save = unit_data["save"]
        self.ward = unit_data.get("ward", None)
        self.champion = unit_data.get("has_champion", True)

        # Initialize weapons
        self.weapons = []
        for weapon_data in unit_data.get("weapons", []):
            weapon = Weapon(**weapon_data)
            self.weapons.append(weapon)
