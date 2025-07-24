import { Link } from 'react-router-dom';
import '../styles/nav_bar.css';

function NavBar() {
  return (
    <nav>
      <p>Age of Sigmath®</p>
      <div className="nav-links">
        <Link to="/" className="nav-link">Home</Link>
        <Link to="/calculator">Calculator</Link>
        <Link to="/units">Units</Link>
      </div>
    </nav>
  );
}

export default NavBar;
