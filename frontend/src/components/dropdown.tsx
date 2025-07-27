import React, { useState } from 'react';
import '../styles/dropdown.css';

interface DropdownMenuProps {
  label: string;
}

const DropdownMenu: React.FC<DropdownMenuProps> = ({ label }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="dropdown_menu">
      <label>{label}</label>
      <button className="dropdown_button" onClick={toggleDropdown}>
        Select {label}
      </button>
      {isOpen && (
        <ul className="dropdown_list">
          <button>Option 1</button>
          <button>Option 2</button>
          <button>Option 3</button>
        </ul>
      )}
    </div>
  );
};

export default DropdownMenu;
