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

#### Setting up the backend
Install FastAPI and uvicorn (should already be done if you installed requirements)
```shell
pip install fastapi uvicorn
```

Start the Development Server
```shell
uvicorn main:app --reload
```

This will start the FastAPI dev server at http://localhost:8000. You can also visit http://localhost:8000/docs to try the automatically generated API interactively.

#### Setting up the frontend
Install node and npm
- Download and install from https://nodejs.org
- Verify installation:

```bash
node -v
npm -v
```

Install Dependencies
```shell
cd frontend/
npm install
```

Start the Development Server
```shell
cd frontend/
npm run dev
```

This will start the Vite dev server. Open your browser and navigate to http://localhost:5173 to view the app.


##### Project Structure

The project uses the standard Vite + React + TypeScript setup. Key folders:

- `src/` – Main source code
- `src/pages/` – Page components
- `src/components/` – Reusable UI components
- `src/assets/` – Static assets (images, fonts, etc.)
- `src/hooks/` – React hooks to handle state-based changes
- `src/styles/` – css files


### Customizing

You can add unit profiles in rules > **unit_profiles.py**

To add a unit to the simulation, insert it in the 'units' array in the **main.py** file

### Special Weapon Rules (supported)

- `"id": "companion"`: Flag the weapon as "companion"
- `"id": "crit_auto_wound"`: Flag the weapon as "Crit Auto Wound"
- `"id": "crit_mortal"`: Flag the weapon as "Crit Mortal"
- `"id": "crit_2_hits"`: Flag the weapon as "Crit 2 Hits"
- `"id": "crit_5+"`: Flag the weapon as "Crit 5+" 
- `"id": "add_X", "condition": Y, , "value": Z`: If condition Y (charged/...) is satified, add Z to value X (attacks, rend, hit, wound)