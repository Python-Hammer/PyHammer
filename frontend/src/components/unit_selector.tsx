import React, { useEffect } from "react";
import DropdownMenu from "./dropdown";
import "../styles/unit_selector.css";
import burgerIcon from "../assets/icon-burger.png";

const UnitSelector = () => {
  const [units, setUnits] = React.useState<string[]>([]);
  const [factions, setFactions] = React.useState<string[]>([]);
  const weapons = ["Sword", "Bow"];
  const [unit, setUnit] = React.useState("");
  const [faction, setFaction] = React.useState("");

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
    </div>
  );
};

export default UnitSelector;
