import React, { useState } from "react";
import "../styles/dropdown.css";

export interface DropdownOption {
  id: string;
  name: string;
}

interface DropdownMenuProps {
  label: string;
  options?: DropdownOption[];
  selection?: string;
  onChange: (value: string) => void;
}

const DropdownMenu: React.FC<DropdownMenuProps> = ({
  label,
  options,
  selection,
  onChange,
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="dropdown_menu">
      <label>{label}</label>
      <select
        value={selection ?? ""}
        onChange={(e) => onChange(e.target.value)}
      >
        <option value="" disabled>
          Select a {label}
        </option>
        {options &&
          options.map((option) => (
            <option key={option.id} value={option.id}>
              {option.name}
            </option>
          ))}
      </select>
    </div>
  );
};

export default DropdownMenu;
