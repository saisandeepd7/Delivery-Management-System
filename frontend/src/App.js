import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ComponentForm from './components/ComponentForm';
import RevenueGraph from './components/RevenueGraph';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/components" element={<ComponentForm />} />
        <Route path="/revenue" element={<RevenueGraph period="daily" />} />
      </Routes>
    </Router>
  );
}

export default App;
