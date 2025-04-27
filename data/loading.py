import json
from pathlib import Path


def load_faction(faction_name: str) -> dict:
    """Load a faction's units from its JSON file"""
    file_path = Path(__file__).parent / f"../data/factions/{faction_name}.json"
    with open(file_path, "r") as f:
        return json.load(f)


def get_all_units() -> dict:
    """Load all available units from all faction files"""
    units_by_id = {}
    faction_dir = Path(__file__).parent / "../data/factions"

    for file_path in faction_dir.glob("*.json"):
        with open(file_path, "r") as f:
            faction_data = json.load(f)
            for unit_data in faction_data.get("units", []):
                units_by_id[unit_data["id"]] = unit_data

    return units_by_id
