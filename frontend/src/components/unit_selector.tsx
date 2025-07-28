import React from 'react';
import DropdownMenu from './dropdown';
import '../styles/unit_selector.css';
import burgerIcon from '../assets/icon-burger.png';


const UnitSelector = () => {
  const units = [ "Steam Tank", "Immortis Guard" ];
  const factions = [ "Order", "Death" ];
  const weapons = [ "Sword", "Bow" ];
  const [unit, setUnit] = React.useState('Steam Tank');
  const [faction, setFaction] = React.useState('Order');
  const [weapon, setWeapon] = React.useState('Sword');

  return (
    <div className="unit_selector">
        <h2>{unit.toUpperCase()}</h2>
        <DropdownMenu
          label="Faction"
          options={factions}
          selection={faction}
          onChange={setFaction}
        />
        <DropdownMenu
          label="Unit"
          options={units}
          selection={unit}
          onChange={setUnit}
        />
        <div className="unit_portrait">
            <img
                src={burgerIcon}
                alt="Unit Portrait"
                className="unit_portrait_img"
            />
            <p>{unit}</p>
        </div>
        <DropdownMenu
          label="Weapon"
          options={weapons}
          selection={weapon}
          onChange={setWeapon}
        />
    </div>
  );
}

export default UnitSelector;
