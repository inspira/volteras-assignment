// Ref: https://www.taniarascia.com/front-end-tables-sort-filter-paginate/

import PropTypes from 'prop-types';
import React from 'react';

function Table({ columns, rows }) {
  return (
    <table>
      <thead>
        <tr>
          {columns.map((column) => <th key={column.accessor}>{column.label}</th>)}
        </tr>
      </thead>
      <tbody>
        {rows.map((row) => (
          <tr key={row.id}>
            {columns.map((column) => {
              if (column.format) {
                return <td key={column.accessor}>{column.format(row[column.accessor])}</td>;
              }
              return <td key={column.accessor}>{row[column.accessor]}</td>;
            })}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

Table.propTypes = {
  columns: PropTypes.arrayOf(
    PropTypes.shape({
      accessor: PropTypes.string,
      label: PropTypes.string,
    }),
  ).isRequired,
  rows: PropTypes.any,
};

Table.defaultProps = {
  rows: [],
};

export default Table;
