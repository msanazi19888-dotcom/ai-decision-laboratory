import { NavLink } from "react-router-dom";
import { FaBrain } from "react-icons/fa";

function Navigation() {
  return (
    <header className="app-header">
      <div className="app-brand">
        <div className="brand-logo">
          <FaBrain />
        </div>

        <div>
          <h1>AI Decision Laboratory</h1>
          <p>Decision Intelligence Platform</p>
        </div>
      </div>

      <nav className="navigation">
        <NavLink
          to="/"
          className={({ isActive }) =>
            isActive ? "nav-link active" : "nav-link"
          }
        >
          Dashboard
        </NavLink>

        <NavLink
          to="/history"
          className={({ isActive }) =>
            isActive ? "nav-link active" : "nav-link"
          }
        >
          Decision History
        </NavLink>
      </nav>
    </header>
  );
}

export default Navigation;