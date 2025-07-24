import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/home';
import UnitListPage from './pages/units';
import CalculatorPage from './pages/calculator';
import NavBar from './components/nav_bar';

function App() {
  return (
    <>
      <NavBar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/units" element={<UnitListPage />} />
        <Route path="/calculator" element={<CalculatorPage />} />
      </Routes>
    </>
  );
}

export default App;
