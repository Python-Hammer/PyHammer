from models.profile import Profile


def simulate_combat(
    attacker: Profile,
    defender: Profile,
    attacker_context_dict: dict = None,
    defender_context_dict: dict = None,
) -> dict:
    """
    Simulate a combat between two profiles.
    The attacker and defender are instances of the Profile class.
    The combat_context_dict can include additional information like situational buffs,
    debuffs, mortal damage on top of the fight, etc.
    The attacker_context_dict (respectively defender) includes everything relevant to their attacks and saves
    (be it buffs from the attacker or debuffs from the defender).
    """

    attacker_damage = attacker.attack_with_all_weapons(attacker_context_dict, defender.save)
    defender_models_slain = defender.receive_damage(attacker_damage)

    defender_damage = defender.attack_with_all_weapons(defender_context_dict, attacker.save)
    attacker_models_slain = attacker.receive_damage(defender_damage)

    return {
        "attacker": {
            "models_slain": attacker_models_slain,
            "remaining_models": attacker.current_models,
            "damage_received": defender_damage,
        },
        "defender": {
            "models_slain": defender_models_slain,
            "remaining_models": defender.current_models,
            "damage_received": attacker_damage,
        },
    }


from models.profile import Profile
from data.loading import get_all_units
import numpy as np

varanguard_dict = get_all_units()["varanguard"]
stoneguard_dict = get_all_units()["alarith_stoneguard"]


damage_inflicted_chaos_knight_attack = []
damage_inflicted_stoneguard_defense = []

damage_inflicted_stoneguard_attack = []
damage_inflicted_chaos_knight_defense = []

for i in range(10000):

    chaos_knights = Profile(varanguard_dict, is_reinforced=True)
    stoneguard = Profile(stoneguard_dict, is_reinforced=True)

    attacker_context = {"charged": True, "add_rend": -2, "ward": 5, "add_to_hit": 1, "add_save": 1}
    defender_context = {"add_rend": 1}
    chaos_attack_fight = simulate_combat(
        chaos_knights,
        stoneguard,
        attacker_context_dict=attacker_context,
        defender_context_dict=defender_context,
    )
    damage_inflicted_chaos_knight_attack.append(chaos_attack_fight["defender"]["damage_received"])
    damage_inflicted_stoneguard_defense.append(chaos_attack_fight["attacker"]["damage_received"])

print(f"Chaos Knight attack: {np.max(damage_inflicted_chaos_knight_attack):.2f} damage inflicted")
print(f"Stoneguard defense: {np.max(damage_inflicted_stoneguard_defense):.2f} damage inflicted")

print(
    (np.array(damage_inflicted_chaos_knight_attack) >= 16).sum() / len(damage_inflicted_chaos_knight_attack)
)

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for nicer plots
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))

# Create a figure with two subplots (side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

sns.histplot(
    damage_inflicted_chaos_knight_attack, ax=ax1, kde=True, color="red", alpha=0.6, stat="probability"
)
ax1.set_title("Damage Distribution: Chaos Knights Attack")
ax1.set_xlabel("Damage")
ax1.set_ylabel("Probability")

sns.histplot(
    damage_inflicted_stoneguard_defense, ax=ax2, kde=True, color="blue", alpha=0.6, stat="probability"
)
ax2.set_title("Damage Distribution: Stoneguard Defense")
ax2.set_xlabel("Damage")
ax2.set_ylabel("Probability")

plt.tight_layout()
plt.show()

# Alternative: Create a violin plot comparing both distributions
plt.figure(figsize=(10, 6))
plot_data = {
    "Chaos Knights Attack": damage_inflicted_chaos_knight_attack,
    "Stoneguard Defense": damage_inflicted_stoneguard_defense,
}
sns.violinplot(data=plot_data)
plt.title("Damage Distribution Comparison")
plt.ylabel("Damage")
plt.show()

# Print summary statistics
print(
    f"Chaos Knights Attack: Mean={np.mean(damage_inflicted_chaos_knight_attack):.2f}, Median={np.median(damage_inflicted_chaos_knight_attack):.2f}"
)
print(
    f"Stoneguard Defense: Mean={np.mean(damage_inflicted_stoneguard_defense):.2f}, Median={np.median(damage_inflicted_stoneguard_defense):.2f}"
)
