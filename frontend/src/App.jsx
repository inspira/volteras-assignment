import './App.css';
import React, { useState, useEffect } from 'react';
import qs from 'qs';
import Chart from './Chart';
import Table from './Table';
import Pagination from './Pagination';

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
  // api calls
  const [data, setData] = useState();
  const [apiUri, setApiUri] = useState();
  const [error, setError] = useState();

  // filter
  const [vehicleId, setVehicleId] = useState('');

  // paging
  const [activePage, setActivePage] = useState(1);
  const [totalItems, setTotalItems] = useState(0);
  const rowsPerPage = 10;

  // sorting
  const [sort, setSort] = useState({ order: 'asc', orderBy: 'timestamp' });

  function loadData(vId) {
    const params = {
      vehicle_id: vId,
      page_size: rowsPerPage,
      page_index: activePage,
      sort_by: sort.orderBy,
      sort_order: sort.order,
    };
    const queryString = qs.stringify(params);

    const uri = `${API_PATH}/vehicle_data/?${queryString}`;
    setApiUri(uri);

    fetch(uri)
      .then((response) => {
        if (response.status !== 200) {
          throw new Error(`${response.status} ${response.statusText}`);
        }
        const bodyObj = response.json();
        return bodyObj;
      })
      .then((jsonData) => {
        setData(jsonData.data);
        setTotalItems(jsonData.total_items);
      })
      .catch((err) => {
        setError(`${err}`);
      });
  }

  // This is calling the API twice because of a new behavior of
  // React 18 when React.StrictMode is enabled in development mode
  // See also: https://beta.reactjs.org/learn/synchronizing-with-effects
  useEffect(() => {
    loadData(vehicleId, activePage, sort);
  }, [vehicleId, activePage, sort]);

  const selectedVehicleCaption = (vehicleId !== '' ? vehicleId : 'all vehicles');

  return (
    <div className="App">
      <header className="App-header">
        <h1>Volteras Vehicle Data</h1>
      </header>
      <div className="Table-with-filter">
        {/* TODO: Encapsulate this dropdown in a component */}
        <select
          value={vehicleId}
          onChange={(event) => {
            setVehicleId(event.target.value);
            setActivePage(1);
          }}
          className="Vehicle-Dropdown"
          name="Vehicle-Dropdown"
        >
          {/* TODO: Retrieve this list from an API */}
          <option value="">All vehicle IDs</option>
          <option value="06ab31a9-b35d-4e47-8e44-9c35feb1bfae">06ab31a9-b35d-4e47-8e44-9c35feb1bfae</option>
          <option value="1bbdf62b-4e52-48c4-8703-5a844d1da912">1bbdf62b-4e52-48c4-8703-5a844d1da912</option>
          <option value="f212b271-f033-444c-a445-560511f95e9c">f212b271-f033-444c-a445-560511f95e9c</option>
        </select>
      </div>
      <div>
        <p>
          {`Data points for ${selectedVehicleCaption}`}
        </p>
        {
          error && (
            <p>
              {error}
            </p>
          )
        }
      </div>
      <div className="Table">
        <Table rows={data} columns={columns} sort={sort} onSort={setSort} />
        <Pagination
          activePage={activePage}
          totalItems={totalItems}
          rowsPerPage={rowsPerPage}
          setActivePage={setActivePage}
        />
        <p>
          activePage={activePage}<br />
          totalItems={totalItems}<br />
          rowsPerPage={rowsPerPage}
        </p>
      </div>
      <div>
        <p>
          {/* TODO: We should create a specific API operation for exporting data */}
          <a href={apiUri} target="_blank" rel="noopener noreferrer" download>Export as JSON</a>
        </p>
      </div>
      <div className="Chart">
        <Chart data={data} />
      </div>
    </div>
  );
}

export default App;
