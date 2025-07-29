import React, { useEffect } from "react";
import DropdownMenu, { type DropdownOption } from "./dropdown";
import "../styles/unit_selector.css";
import burgerIcon from "../assets/icon-burger.png";

interface UnitSelectorProps {
  onUnitSelect?: (unit: any) => void;
}

const UnitSelector = ({ onUnitSelect }: UnitSelectorProps) => {
  const [units, setUnits] = React.useState<DropdownOption[]>([]);
  const [factions, setFactions] = React.useState<DropdownOption[]>([]);
  const [unit, setUnit] = React.useState("");
  const [faction, setFaction] = React.useState("");

  const getUnitName = (unitId: string): string => {
    const foundUnit = units.find((u) => u.id === unitId);
    return foundUnit ? foundUnit.name : "";
  };

  const handleFactionChange = async (factionId: string) => {
    setFaction(factionId);
    setUnit(""); // Reset unit selection when faction changes
    if (onUnitSelect) {
      onUnitSelect(null); // Clear selected unit when faction changes
    }
  };

  const handleUnitChange = async (unitId: string) => {
    setUnit(unitId);
    if (onUnitSelect && unitId) {
      try {
        const response = await fetch(
          `http://localhost:8000/unit_info/${faction}/${unitId}`
        );
        const data = await response.json();
        onUnitSelect(data);
      } catch (error) {
        console.error("Error fetching unit data:", error);
      }
    }
  };

  useEffect(() => {
    const fetchFactions = async () => {
      const response = await fetch("http://localhost:8000/faction_list");
      const data = await response.json();
      setFactions(data);
    };
    fetchFactions();
  }, []);

  useEffect(() => {
    const fetchUnits = async () => {
      if (faction) {
        const response = await fetch(
          `http://localhost:8000/faction_list/${faction}/units`
        );
        const data = await response.json();
        setUnits(data);
      } else {
        setUnits([]);
      }
    };
    fetchUnits();
  }, [faction]);

  return (
    <div className="unit_selector">
      <h2>{getUnitName(unit).toUpperCase()}</h2>
      <DropdownMenu
        label="Faction"
        options={factions}
        selection={faction}
        onChange={handleFactionChange}
      />
      <DropdownMenu
        label="Unit"
        options={units}
        selection={unit}
        onChange={handleUnitChange}
      />
      <div className="unit_portrait">
        <img
          src={burgerIcon}
          alt="Unit Portrait"
          className="unit_portrait_img"
        />
        <p>{getUnitName(unit)}</p>
      </div>
    </div>
  );
};

export default UnitSelector;
