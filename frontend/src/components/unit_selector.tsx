import React from 'react';
import { Link } from 'react-router-dom';
import DropdownMenu from './dropdown';
import '../styles/unit_selector.css';
import burgerIcon from '../assets/icon-burger.png';


const UnitSelector = () => {

  return (
    <div className="unit_selector">
        <h2>Select Your Unit</h2>
        <DropdownMenu label="Select Faction" />
        <DropdownMenu label="Select Unit" />
        <div className="unit_portrait">
            <img
                src={burgerIcon}
                alt="Unit Portrait"
                className="unit_portrait_img"
            />
            <p>Unit Name</p>
        </div>
        <DropdownMenu label="Select Weapon 1" />
        <DropdownMenu label="Select Weapon 2" />
    </div>
  );
}

export default UnitSelector;
