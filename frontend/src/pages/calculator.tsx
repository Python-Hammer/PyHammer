import { useState } from 'react';
import '../styles/calculator_page.css';

// components
import UnitSelector from "../components/unit_selector";
import Card from "../components/card";

const calculator_page = async () => {
  const [attacker, setAttacker] = useState("Steam Tank");
  const [defender, setDefender] = useState("Immortis Guard");
  const [damage, setDamage] = useState<number | null>(null);

  const calculateDamage = async () => {
    const response = await fetch("http://localhost:8000/calculate-damage", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ attacker, defender })
    });

    const data = await response.json();
    setDamage(data.damage);
  }

  return (
    <div className='calculator_page page-container'>
      <h1>CALCULATOR</h1>
      <p>Select 2 units. Then make them BATTLE !</p>
      <div className="calculator_battle_content">
        <UnitSelector />
        <div className='results'>
          <button onClick={calculateDamage}>Battle</button>
          {damage !== null && (
          <Card title="Average damage" content={damage.toString()} />
          )}
          <div className='results_content'>
            <p>Results will be displayed here after battle.</p>
          </div>
        </div>
        <UnitSelector />
      </div>
    </div>
  );
}

export default calculator_page;
