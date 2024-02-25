import "bootstrap/dist/css/bootstrap.min.css"
import Login from './Login'
import Dashboard from './Dashboard';

// get the code from response url
const code = new URLSearchParams(window.location.search).get('code');



function App() {
  return code ? <Dashboard code={code} /> : <Login />
}

export default App;



/* function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App; */
