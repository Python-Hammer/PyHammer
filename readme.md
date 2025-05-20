# AOS

### A small python tool to see how the units from the Age Of Sigmar tabletop wargame compare in a fight

Simulates a number of fights for a list of units then displays graphs with the results

### Quickstart
Setup your virtual environment:
```shell
python -m venv .venv
```

then activate it:
```shell
source .venv/bin/activate
```

install the necessary packages 📦
```shell
pip install -r requirements.txt
```

run 🚀
```shell
python main.py
```

### Customizing

You can add unit profiles in rules > **unit_profiles.py**

To add a unit to the simulation, insert it in the 'units' array in the **main.py** file

### Special Weapon Rules (supported)

- `"id": "companion"`: Flag the weapon as "companion"
- `"id": "auto_wound"`: Flag the weapon as "Auto Wound"
- `"id": "crit_mortal"`: Flag the weapon as "Crit Mortal"
- `"id": "crit_2_hits"`: Flag the weapon as "Crit 2 Hits"
- `"id": "add_X", "condition": Y, , "value": Z`: If condition Y (charged/...) is satified, add Z to value X (attacks, rend, hit, wound)