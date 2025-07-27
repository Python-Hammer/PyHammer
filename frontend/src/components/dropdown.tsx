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
      <button className="dropdown_button" onClick={toggleDropdown}>
        {label}
      </button>
      {isOpen && (
        <ul className="dropdown_list">
          <li><a href="#">Option 1</a></li>
          <li><a href="#">Option 2</a></li>
          <li><a href="#">Option 3</a></li>
        </ul>
      )}
    </div>
  );
};

export default DropdownMenu;
