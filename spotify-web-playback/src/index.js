import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';


// function HelloWorld() {
//   return <h1 className="greeting">Hello, world!</h1>;
// }


ReactDOM.render(
  <React.StrictMode>
    {/* <HelloWorld /> */}
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
