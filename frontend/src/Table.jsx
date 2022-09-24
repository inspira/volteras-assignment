// Ref: https://www.taniarascia.com/front-end-tables-sort-filter-paginate/

import PropTypes from 'prop-types';
import { React } from 'react';

const handleSort = (onSort, accessor) => {
  onSort((prevSort) => ({
    order: prevSort.order === 'asc' && prevSort.orderBy === accessor ? 'desc' : 'asc',
    orderBy: accessor,
  }));
};

function Table({
  columns, rows, sort, onSort,
}) {
  return (
    <table className="styled-table">
      <thead>
        <tr>
          {/* TODO: extract method */}
          {columns.map((column) => {
            const sortIcon = () => {
              if (column.accessor === sort.orderBy) {
                if (sort.order === 'asc') {
                  return '⬆️';
                }
                return '⬇️';
              }
              return '️↕️';
            };

            return (
              <th key={column.accessor}>
                <span>{column.label}</span>
                <button type="button" onClick={() => handleSort(onSort, column.accessor)}>{sortIcon()}</button>
              </th>
            );
          })}
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
  sort: PropTypes.shape({
    order: PropTypes.string,
    orderBy: PropTypes.string,
  }).isRequired,
  onSort: PropTypes.func.isRequired,
};

Table.defaultProps = {
  rows: [],
};

export default Table;
