import base64
from fastapi import APIRouter
import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend for matplotlib
import matplotlib.pyplot as plt

from metrics.unit_metric import AlphaStrike, average_metric, plot_cdf
from models.profile import Profile


router = APIRouter()


@router.post("/calculate-damage")
def calculate_damage(attacker: dict, defender: dict):
    result = {}
    attacker_profile = Profile(attacker)
    defender_profile = Profile(defender)

    attacker_context = {f"enemy_{type}": True for type in defender_profile.unit_type}

    metric = AlphaStrike(ennemy_unit=defender_profile, return_n_slain_models=False, scale_by_cost=False)
    result["average_damage"] = average_metric(
        attacker_profile, metric, n_samples=5000, combat_context=attacker_context
    )
    img_buffer = plot_cdf(attacker_profile, metric, n_samples=1000, combat_context=attacker_context)
    img_buffer.seek(0)
    result["plot_cdf"] = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
    plt.close()

    return result
