// UnitStatsCard.tsx
import React from "react";
import "../styles/unit_stats_card.css";

interface Unit {
  id: string;
  name: string;
  point_cost: number;
  model_count: number;
  unit_type: string | string[];
  health: number;
  save: number;
  ward?: number;
  has_champion?: boolean;
  weapons: Weapon[];
  abilities?: Ability[];
}

interface Weapon {
  name: string;
  attacks: number;
  to_hit: number;
  to_wound: number;
  damage: string;
  rend: number;
  special_rules?: SpecialRule[];
}

interface SpecialRule {
  id: string;
  condition?: string;
  value?: number;
}

interface Ability {
  name: string;
  id: string;
  damage?: number;
  roll?: string;
}

interface UnitStatsCardProps {
  unit: Unit | null;
}

const UnitStatsCard: React.FC<UnitStatsCardProps> = ({ unit }) => {
  if (!unit) {
    return (
      <div className="unit_stats_card empty">
        <p>No unit selected</p>
      </div>
    );
  }

  const formatUnitType = (type: string | string[]) => {
    return Array.isArray(type) ? type.join(", ") : type;
  };

  const formatSpecialRules = (rules: SpecialRule[] = []) => {
    return rules
      .map((rule) => {
        let ruleText = rule.id.replace("_", " ").toUpperCase();
        if (rule.condition) ruleText += ` vs ${rule.condition.toUpperCase()}`;
        if (rule.value) ruleText += ` (+${rule.value})`;
        return ruleText;
      })
      .join(", ");
  };

  return (
    <div className="unit_stats_card">
      <div className="unit_header">
        <h3 className="unit_name">{unit.name}</h3>
        <div className="unit_meta">
          <span className="point_cost">{unit.point_cost} pts</span>
          <span className="model_count">{unit.model_count} models</span>
          <span className="unit_type">{formatUnitType(unit.unit_type)}</span>
        </div>
      </div>

      <div className="unit_defensive_stats">
        <div className="stat_group">
          <span className="stat_label">Health:</span>
          <span className="stat_value">{unit.health}</span>
        </div>
        <div className="stat_group">
          <span className="stat_label">Save:</span>
          <span className="stat_value">{unit.save}+</span>
        </div>
        {unit.ward && (
          <div className="stat_group">
            <span className="stat_label">Ward:</span>
            <span className="stat_value">{unit.ward}+</span>
          </div>
        )}
        {unit.has_champion && (
          <div className="stat_group">
            <span className="champion_indicator">★ Champion</span>
          </div>
        )}
      </div>

      <div className="weapons_section">
        <h4>Weapons</h4>
        {unit.weapons.map((weapon, index) => (
          <div key={index} className="weapon_card">
            <h5 className="weapon_name">{weapon.name}</h5>
            <div className="weapon_stats">
              <div className="weapon_stat">
                <span className="label">A:</span>
                <span className="value">{weapon.attacks}</span>
              </div>
              <div className="weapon_stat">
                <span className="label">Hit:</span>
                <span className="value">{weapon.to_hit}+</span>
              </div>
              <div className="weapon_stat">
                <span className="label">Wound:</span>
                <span className="value">{weapon.to_wound}+</span>
              </div>
              <div className="weapon_stat">
                <span className="label">Rend:</span>
                <span className="value">-{weapon.rend}</span>
              </div>
              <div className="weapon_stat">
                <span className="label">Dmg:</span>
                <span className="value">{weapon.damage}</span>
              </div>
            </div>
            {weapon.special_rules && weapon.special_rules.length > 0 && (
              <div className="special_rules">
                <span className="special_rules_label">Special:</span>
                <span className="special_rules_text">
                  {formatSpecialRules(weapon.special_rules)}
                </span>
              </div>
            )}
          </div>
        ))}
      </div>

      {unit.abilities && unit.abilities.length > 0 && (
        <div className="abilities_section">
          <h4>Abilities</h4>
          {unit.abilities.map((ability, index) => (
            <div key={index} className="ability_card">
              <h5 className="ability_name">{ability.name}</h5>
              <div className="ability_details">
                {ability.roll && <span>Roll: {ability.roll}</span>}
                {ability.damage && <span>Damage: {ability.damage}</span>}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default UnitStatsCard;
