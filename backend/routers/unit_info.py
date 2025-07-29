from fastapi.routing import APIRouter

from data import FACTION_NAME_MAPPING
from data.loading import get_all_units, get_faction_names

router = APIRouter()


@router.get("/unit_info/{faction}/{unit_name}")
async def get_unit_info(faction: str, unit_name: str) -> dict:
    """
    Returns detailed information about a specific unit.
    """
    units = get_all_units(faction_name=faction)
    unit_info = units.get(unit_name)
    if not unit_info:
        return {"error": "Unit not found"}
    return unit_info
