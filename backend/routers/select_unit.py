from data import FACTION_NAME_MAPPING
from data.loading import get_all_units, get_faction_names
from fastapi import APIRouter

router = APIRouter()


@router.get("/faction_list")
async def get_faction_list() -> list[str]:
    """
    Returns a list of all available factions.
    """
    return get_faction_names()


@router.get("/faction_list/{faction_name}/units")
async def get_units_by_faction(faction_name: str) -> list[str]:
    """
    Returns a list of all units for a given faction.
    """
    units = get_all_units(faction_name=FACTION_NAME_MAPPING[faction_name])
    return [unit["name"] for unit in units.values()]
