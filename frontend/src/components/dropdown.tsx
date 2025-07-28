import React, { useState } from 'react';
import '../styles/dropdown.css';

interface DropdownMenuProps {
  label: string;
  options?: string[];
  selection?: string;
  onChange: (value: string) => void;
}

const DropdownMenu: React.FC<DropdownMenuProps> = ({ label, options, selection, onChange }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="dropdown_menu">
      <label>{label}</label>
      {/* <button className="dropdown_button" onClick={toggleDropdown}>
        Select {label}
      </button> */}
      {/* {isOpen && (
        <ul className="dropdown_list">
          {units.map((unit) => (
            <li key={unit}>
              <button onClick={(e) => onChange(e.target.value)}>{unit}</button>
            </li>
          ))}
        </ul>
      )} */}
      <select value={selection ?? ""} onChange={(e) => onChange(e.target.value)}>
        <option value="" disabled>Select a {label}</option>
        {options && options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>

    </div>
  );
};

export default DropdownMenu;
