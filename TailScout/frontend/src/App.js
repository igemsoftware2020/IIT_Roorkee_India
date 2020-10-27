import { BrowserRouter, Link } from "react-router-dom"
import Router from './routes'

import './App.css';

function App() {
  return (
    <BrowserRouter>

      <header>
        <nav className="navbar navbar-expand-md navbar-light fixed-top bg-light">
          <Link className="navbar-brand nav-logo" to="/">
            <img
              src="/assets/icon/igem.png"
              alt="iGEM Logo"
              className="nav-logo-image"
            />
            <div>TailScout</div>
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarCollapse"
            aria-controls="navbarCollapse"
            aria-expanded="false"
            aria-label="Toggle navigation"
            style={{
              width: 'auto',
              margin: "auto 0"
            }}
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarCollapse">
            <ul className="navbar-nav ml-auto">
              <li className="nav-item active">
                <Link className="nav-link" to="/">
                  Home <span className="sr-only">(current)</span>
                </Link>
              </li>
              <li className="nav-item">
                <a
                  className="nav-link"
                  href="https://2020.igem.org/Team:IIT_Roorkee/Team"
                >
                  Team
                </a>
              </li>
              <li className="nav-item">
                <a
                  className="nav-link"
                  href="https://github.com/igemsoftware2020/IIT_Roorkee_India"
                >
                  Contribute
                </a>
              </li>
            </ul>
          </div>
        </nav>
      </header>

      <Router />

      <footer className="footer container">
        <p style={{ textAlign: "center" }}>Made with ❤️ by iGEM IIT Roorkee</p>
      </footer>

    </BrowserRouter>

  );
}

export default App;
