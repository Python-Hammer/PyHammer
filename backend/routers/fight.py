from fastapi import APIRouter

from metrics.unit_metric import AlphaStrike, average_metric
from models.profile import Profile


router = APIRouter()


@router.post("/calculate-damage")
async def calculate_damage(
    attacker: dict, defender: dict, attacker_context: dict = None, defender_context: dict = None
):
    if attacker_context is None:
        attacker_context = {}
    if defender_context is None:
        defender_context = {}

    attacker_profile = Profile(attacker)
    defender_profile = Profile(defender)

    metric = AlphaStrike(ennemy_unit=defender_profile, return_n_slain_models=False, scale_by_cost=False)
    result = average_metric(attacker_profile, metric)

    return result
