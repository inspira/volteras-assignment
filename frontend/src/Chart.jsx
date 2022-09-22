import PropTypes from 'prop-types';
import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Vehicle data',
    },
  },
};

function Chart({ data }) {
  const labels = data.map((point) => point.timestamp);
  const points = {
    labels,
    datasets: [
      {
        label: 'Speed',
        data: data.map((point) => point.speed),
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
      {
        label: 'Elevation',
        data: data.map((point) => point.elevation),
        borderColor: 'rgb(53, 162, 235)',
        backgroundColor: 'rgba(53, 162, 235, 0.5)',
      },
    ],
  };
  return <Line options={options} data={points} />;
}

Chart.propTypes = {
  data: PropTypes.any,
};

Chart.defaultProps = {
  data: [],
};

export default Chart;
