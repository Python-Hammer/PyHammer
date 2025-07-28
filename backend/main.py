from rules.unit_profiles import *
from metrics.unit_metric import *
import numpy as np
from data.loading import get_all_profiles, get_all_units
from models.profile import Profile

np.set_printoptions(precision=2, suppress=True)


def main():
    ################ Load all units ################

    all_units = get_all_units()
    knights = Profile(all_units["chaos_knights_charge"], is_reinforced=False)
    dawnriders = Profile(all_units["scourge_of_ghyran_light_of_eltharion"])

    ################ Print a metric ################

    metric = AlphaStrike(ennemy_unit=knights, scale_by_cost=False)
    # metric = DPS(save=4, scale_by_cost=False)
    # metric = AlphaStrike(ennemy_unit=knights, scale_by_cost=False)
    # print(average_metric(units[1], metric, n_samples=10000))
    multi_unit_plot_cdf([dawnriders, knights], metric, n_samples=10000)
    # plot_cdf(dawnriders, metric, n_samples=10000)
    """
    ################ Plot different metrics ################
     
    metrics = [DPS(save=s, scale_by_cost=True) for s in [2, 3, 4, 5]]
    multimetric_plot(units, metrics, n_samples=10000)

    
    ################ Plot different metrics ################
     
    metrics = [DPS(save=s, samples=100, scale_by_cost=True) for s in [2, 3, 4, 5]]
   
    multimetric_plot(units, metrics)
    
    ################ Tournament ################

    metric = winrate(samples=100, initiative=1)

    matrix(units, metric)


    ################ Ranking according to a metric ################

    metric = DPS(save=3, samples=100)

    print(ranking(units, metric))
    """


if __name__ == "__main__":
    main()
