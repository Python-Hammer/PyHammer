import '../styles/calculator_page.css';

// components
import UnitSelector from "../components/unit_selector";
import Card from "../components/card";

function calculator_page() {
  return (
    <div className='calculator_page page-container'>
      <h1>CALCULATOR</h1>
      <p>Select 2 units. Then make them BATTLE !</p>
      <div className="calculator_battle_content">
        <UnitSelector />
        <div className='results'>
          <button>Battle</button>
          <Card title="Average damage" content="1.0" />
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
