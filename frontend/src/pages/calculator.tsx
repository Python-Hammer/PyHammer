import { useState, type ReactElement } from "react";
import "../styles/calculator_page.css";

// components
import UnitSelector from "../components/unit_selector";
import UnitStatsCard from "../components/unit_stats_card";
import { getUnitForApi } from "../components/unit_stats_card";
import Card from "../components/card";

const calculator_page = () => {
  const [attackerUnit, setAttackerUnit] = useState(null);
  const [defenderUnit, setDefenderUnit] = useState(null);
  const [damage, setDamage] = useState<number | null>(null);
  const [plot, setPlot] = useState<ReactElement | null>(null);

  const calculateDamage = async () => {
    const response = await fetch("http://localhost:8000/calculate-damage", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        attacker: getUnitForApi(attackerUnit),
        defender: getUnitForApi(defenderUnit),
      }),
    });

    const data = await response.json();
    setDamage(data.average_damage);
    setPlot(data.plot_cdf);
  };

  return (
    <div className="calculator_page page-container">
      <div className="calculator_header">
        <h1>CALCULATOR</h1>
        <p>Select 2 units. Then make them BATTLE !</p>
      </div>
      <div className="calculator_battle_content">
        <div className="unit_section_left">
          <UnitSelector onUnitSelect={setAttackerUnit} />
          <UnitStatsCard unit={attackerUnit} />
        </div>
        <div className="results">
          <button onClick={calculateDamage}>Battle</button>
          {damage !== null && (
            <Card title="Average damage" content={damage.toString()} />
          )}
          {plot && (
            <div className="plot_container">
              <h2>CDF Plot</h2>
              <div className="plot_content">
                <img
                  src={`data:image/png;base64,${plot}`}
                  alt="CDF Plot"
                  className="plot_image"
                />
              </div>
            </div>
          )}
          <div className="results_content">
            <p>Results will be displayed here after battle.</p>
          </div>
        </div>
        <div className="unit_section_right">
          <UnitSelector onUnitSelect={setDefenderUnit} />
          <UnitStatsCard unit={defenderUnit} />
        </div>
      </div>
    </div>
  );
};

export default calculator_page;
