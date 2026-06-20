import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/dashboard";
import Login from "./pages/login";
import Register from "./pages/register";
import Tasks from "./pages/Tasks";
import Problems from "./pages/Problems";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/tasks" element={<Tasks />} />
        <Route path="/problems" element={<Problems />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;