from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from damage_calculator import calculate_damage
from unit_data import get_unit_stats

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DamageRequest(BaseModel):
    attacker: str
    defender: str

@app.post("/calculate-damage")
def calculate_damage_endpoint(request: DamageRequest):
    attacker_stats = get_unit_stats(request.attacker)
    defender_stats = get_unit_stats(request.defender)

    if not attacker_stats or not defender_stats:
        raise HTTPException(status_code=404, detail="Unit not found")

    damage = calculate_damage(attacker_stats, defender_stats)
    return {"damage": damage}
