from rules.unit_profiles import *
from metrics.unit_metric import *
from metrics.pairwise_metric import *
import numpy as np
from data.loading import get_all_profiles

np.set_printoptions(precision=2, suppress=True)


def main():
    ################ Load all units ################

    all_units = get_all_profiles(is_reinforced=False)

    ################ Define Units to study ################

    units = [all_units["chaos_knights_charge"], all_units["Chaos_Lord_on_Daemonic_Mount"]]

    ################ Print a metric ################

    metric = BetaStrike(ennemy_unit=all_units["chaos_knights"], scale_by_cost=False)
    #metric = DPS(save=3, scale_by_cost=True)
    multi_unit_plot_cdf(units, metric, n_samples=100000)

    """
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

"""
import numpy as np
from rules.unit_profiles import *
np.set_printoptions(precision=2, suppress=True)

def get_dps(unit):
    #saves = np.array([2,3,4,5])
    saves = np.array([2,3])
    dps = []
    for save in saves:
        samples = 10000
        dps.append(unit.DPS(save, samples).mean())
    dps = np.array(dps)
    return dps


units = [ChaosKnights_Charge(), ChaosKnights_Vanilla(), Varanguard_Charge(), Varanguard_Vanilla(),  
         ChaosLord(), DemonPrince(), Abraxia_Vanilla(), Abraxia_Medium(), Abraxia_All(), Karkadrak_Charge(), Karkadrak_Vanilla(), 
        ChaosLordMounted_Charge(), ChaosLordMounted_Vanilla(),
         Chosen(), ChaosWarriors(),Ogroids(),ChaosChariot(),
         Warden(),Stoneguard(),Eltharion(),Avalenor(), Belakor(), Slautherbrute()]

#units = [Stoneguard(), Stoneguard_11(), Stoneguard_rend1()]


units = [ChaosKnights_Charge(), ChaosKnights_Vanilla(),
        Varanguard_Charge(), Varanguard_Vanilla(), 
        Karkadrak_Charge(), Karkadrak_Vanilla(),
        ChaosLordMounted_Charge(), ChaosLordMounted_Vanilla()]


dps_list = []
name_list = []

for unit in units:
    print(f'Unit: {unit.name}. Dmg/cost:')
    dps = 10*get_dps(unit)/unit.cost
    #print(unit.get_tankiness_modifier(rend=1))
    dps = unit.get_tankiness_modifier(rend=1)*get_dps(unit)/unit.cost
    print(dps)
    dps_list.append(dps)
    name_list.append(unit.name)

sorted_dps_list, sorted_name_list = zip(*sorted(zip(dps_list, name_list), reverse=True))

print(sorted_name_list)
"""
