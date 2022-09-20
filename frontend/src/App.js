import './App.css';
import Table from './Table'
import React, { useState, useEffect } from 'react';

const columns = [
  { accessor: 'timestamp', label: 'Timestamp' },
  { accessor: 'speed', label: 'Speed (km/h)' },
  { accessor: 'odometer', label: 'Odometer (km)' },
  { accessor: 'soc', label: 'State of Charge' },
  { accessor: 'elevation', label: 'Elevation (m)' },
  { accessor: 'shift_state', label: 'Shift State' },
];

function App() {

  const [data, setData] = useState();

  function loadData() {
    fetch("data/vehicle-data.json", { headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }}).then(response => response.json())
        .then(jsonData => setData(jsonData))
        .catch((error) => {
          console.error(error);
        });
  }

  useEffect(() => {
    if(data === undefined){
      loadData()
    }
  }, [data])

  return data && (
    <div className="App">
      <header className="App-header">
        <h1>
          Volteras Vehicle Data
        </h1>
      </header>
      <Table rows={data} columns={columns} />
    </div>
  );
}

export default App;
