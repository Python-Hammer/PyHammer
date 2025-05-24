from .utils import plot_multi_bars
import matplotlib.pyplot as plt
import numpy as np

class unit_metric:
    def __init__(self, samples=1000):
        self.samples = samples
        self.metric_name = "metric name"

    def get_sample(self, unit):
        return 0


def average_metric(unit, metric, n_samples=1000):
    unit.reset()
    metric_value = 0
    for _ in range(n_samples):
        metric_value += metric.get_sample(unit)
    return metric_value / n_samples

def plot_cdf(unit, metric, n_samples=1000):
    unit.reset()
    metric_values = []
    for _ in range(n_samples):
        metric_values.append(metric.get_sample(unit))
    metric_values = np.array(metric_values)
    metric_values = -np.sort(-metric_values)
    yvals = np.arange(len(metric_values)) / float(len(metric_values))
    plt.plot(metric_values, yvals, label=unit.name)
    plt.fill_between(metric_values, yvals, alpha=0.3)
    plt.xlabel(metric.metric_name)
    plt.ylabel("Cumulative Probability")
    plt.legend()
    plt.grid()
    plt.show()

def multi_unit_plot_cdf(units, metric, n_samples=1000):
    plt.figure(figsize=(10, 6))
    L = []
    for unit in units:
        unit.reset()
        metric_values = []
        for _ in range(n_samples):
            metric_values.append(metric.get_sample(unit))
        metric_values = np.array(metric_values)
        metric_values = -np.sort(-metric_values)
        yvals = np.arange(len(metric_values)) / float(len(metric_values))
        avg = np.mean(metric_values)
        L.append({"unit": unit.name, "avg": avg, "metric_values": metric_values, "yvals": yvals})
    L.sort(key=lambda x: x["avg"], reverse=True)
    for dic in L:
        metric_values = dic["metric_values"]
        yvals = dic["yvals"]
        unit = dic["unit"]
        plt.plot(metric_values, yvals, label=unit)    
        plt.fill_between(metric_values, yvals, alpha=0.3)
    plt.xlabel(metric.metric_name)
    plt.ylabel("Cumulative Probability")
    plt.legend()
    plt.grid()
    plt.show()
    
def ranking(units, metric, n_samples=1000):
    units_metrics = []
    units_names = []
    for unit in units:
        units_metrics.append(average_metric(unit, metric, n_samples))
        units_names.append(unit.name)

    sorted_metric_list, sorted_unit_list = zip(*sorted(zip(units_metrics, units_names), reverse=True))

    return sorted_unit_list


def multimetric_plot(units, metrics, n_samples=1000):
    dic_of_dic = {}  # dic[metric_name][unit_name] = metric_value
    for metric in metrics:
        dic_of_dic[metric.metric_name] = {}
        for unit in units:
            dic_of_dic[metric.metric_name][unit.name] = average_metric(unit, metric, n_samples)
    plot_multi_bars(dic_of_dic)


class DPS(unit_metric):
    def __init__(self, save, scale_by_cost=False):
        self.save = save
        self.scale_by_cost = scale_by_cost
        self.metric_name = "DPS vs " + str(save) + "+"

    def get_sample(self, unit, combat_context={}):
        dmg = unit.attack_with_all_weapons(combat_context=combat_context, enemy_save=self.save)
        return dmg / unit.cost if self.scale_by_cost else dmg

class AlphaStrike(unit_metric):
    def __init__(self, ennemy_unit, return_n_slain_models=True, scale_by_cost=False):
        self.ennemy_unit = ennemy_unit
        self.scale_by_cost = scale_by_cost
        self.return_n_slain_models = return_n_slain_models
        self.metric_name = f"Alpha strike vs {ennemy_unit.name} (number of slain models)" if return_n_slain_models else f"Alpha strike vs {ennemy_unit.name} (damage)"

    def get_sample(self, unit, combat_context={}):
        ennemy_unit = self.ennemy_unit
        ennemy_unit.reset()
        dmg = unit.attack_with_all_weapons(combat_context=combat_context, enemy_save=ennemy_unit.save)
        if self.return_n_slain_models:
            metric = ennemy_unit.receive_damage(dmg)
        else:
            metric = dmg
        return metric if self.scale_by_cost else metric

class BetaStrike(unit_metric):
    def __init__(self, ennemy_unit, return_n_slain_models=True, scale_by_cost=False):
        self.ennemy_unit = ennemy_unit
        self.scale_by_cost = scale_by_cost
        self.return_n_slain_models = return_n_slain_models
        self.metric_name = f"Alpha strike vs {ennemy_unit.name} (number of slain models)" if return_n_slain_models else f"Alpha strike vs {ennemy_unit.name} (damage)"


    def get_sample(self, unit, combat_context={}):
        ennemy_unit = self.ennemy_unit
        self.ennemy_unit.reset()
        unit.reset()
        dmg_taken = ennemy_unit.attack_with_all_weapons(combat_context=combat_context, enemy_save=unit.save)
        unit.receive_damage(dmg_taken)
        dmg = unit.attack_with_all_weapons(combat_context=combat_context, enemy_save=ennemy_unit.save)
        if self.return_n_slain_models:
            metric = ennemy_unit.receive_damage(dmg)
        else:
            metric = dmg
        return metric if self.scale_by_cost else metric