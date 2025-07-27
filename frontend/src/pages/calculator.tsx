import '../styles/calculator.css';
import UnitSelector from "../components/unit_selector";

function calculator_page() {
  return (
    <div className='calculator_page'>
      <h1>Calculator</h1>
      <p>Select 2 units. Then make them BATTLE !</p>
      <div className="calculator_battle_content">
        <UnitSelector />
        <UnitSelector />
      </div>
    </div>
  );
}

export default calculator_page;
