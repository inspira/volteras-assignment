import './App.css';
import React, { useState, useEffect } from 'react';
import Table from './Table';

const columns = [
  { accessor: 'timestamp', label: 'Timestamp' },
  { accessor: 'speed', label: 'Speed (km/h)' },
  { accessor: 'odometer', label: 'Odometer (km)' },
  { accessor: 'soc', label: 'State of Charge', format: (value) => `${value}%` },
  { accessor: 'elevation', label: 'Elevation (m)' },
  { accessor: 'shift_state', label: 'Shift State' },
];

// TODO: move to a config file
const API_PATH = '//localhost:8000/api/v1';

function App() {
  const [data, setData] = useState();
  const [error, setError] = useState();

  function loadData() {
    fetch(`${API_PATH}/vehicle_data`)
      .then((response) => response.json())
      .then((jsonData) => setData(jsonData))
      .catch((err) => {
        setError(`Failed to load data: ${err}`);
      });
  }

  // This is calling the API twice because of a new behavior of
  // React 18 when React.StrictMode is enabled in development mode
  // See also: https://beta.reactjs.org/learn/synchronizing-with-effects
  useEffect(() => {
    loadData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Volteras Vehicle Data</h1>
      </header>
      <Table rows={data || []} columns={columns} />
      <p>{error}</p>
    </div>
  );
}

export default App;
