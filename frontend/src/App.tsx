import { Routes, Route } from 'react-router-dom';

// pages
import HomePage from './pages/home';
import UnitListPage from './pages/units';
import CalculatorPage from './pages/calculator';

// components
import NavBar from './components/nav_bar';
import Footer from './components/footer';

// styles
import './styles/global.css';

function App() {
  return (
    <>
      <NavBar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/units" element={<UnitListPage />} />
        <Route path="/calculator" element={<CalculatorPage />} />
      </Routes>
      <Footer />
    </>
  );
}

export default App;
