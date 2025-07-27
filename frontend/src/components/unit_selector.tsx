import React from 'react';
import { Link } from 'react-router-dom';
import DropdownMenu from './dropdown';
import '../styles/unit_selector.css';
import burgerIcon from '../assets/icon-burger.png';


const UnitSelector = () => {

  return (
    <div className="unit_selector">
        <h2>UNIT</h2>
        <DropdownMenu label="Faction" />
        <DropdownMenu label="Unit" />
        <div className="unit_portrait">
            <img
                src={burgerIcon}
                alt="Unit Portrait"
                className="unit_portrait_img"
            />
            <p>Unit Name</p>
        </div>
        <DropdownMenu label="Weapon 1" />
        <DropdownMenu label="Weapon 2" />
    </div>
  );
}

export default UnitSelector;
