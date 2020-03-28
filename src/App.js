import React from 'react'
import logo from './logo.svg'
import './App.css'

//https://covidtracking.com/api/
const testsBySTate = 'https://covidtracking.com/api/states/daily'

const testByCounty = 'https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv?referringSource=articleShare'


function App() {




  return (
    <div className="App">
      <header className="App-header">
        <img alt="logo" className="App-logo" src={logo} />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          rel="noopener noreferrer"
          target="_blank"
        >
          Learn React
        </a>
      </header>
    </div>
  )
}

export default App
