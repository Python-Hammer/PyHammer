import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/nav_bar.css';
import burgerIcon from '../assets/icon-burger.png';


const NavBar: React.FC = () => {
  const [isMenuOpen, setIsMenuOpen] = React.useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <nav>
      <p className="logo">AGE OF SIGMATH®</p>
      <div className="nav-links">
        <Link to="/" className="nav-link">Home</Link>
        <Link to="/calculator">Calculator</Link>
        <Link to="/units">Units</Link>
      </div>
      <img
        src={burgerIcon}
        alt="Menu"
        className="burger_icon"
        onClick={toggleMenu}
      />
    </nav>
  );
}

export default NavBar;
