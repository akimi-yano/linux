import React from 'react';
import {Link, Router} from '@reach/router';
import './App.css';
import Greeting from './components/Greeting.jsx';
import ClassExample from './components/ClassExample.jsx'
function App() {
  return (
    <div className="App">
      <p>Hello World</p>
      <ClassExample />
      <Router>
      <Greeting path='bye'/>
      </Router>
    </div>
  );
}

export default App;
