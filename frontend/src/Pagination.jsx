// Ref: https://www.taniarascia.com/front-end-tables-sort-filter-paginate/

import PropTypes from 'prop-types';
import React from 'react';

function Pagination({
  activePage, totalItems, rowsPerPage, setActivePage,
}) {
  const totalPages = Math.ceil(totalItems / rowsPerPage);
  const beginning = activePage === 1 ? 1 : rowsPerPage * (activePage - 1) + 1;
  const end = activePage === totalPages ? totalItems : beginning + rowsPerPage - 1;

  return (
    <>
      <div className="pagination">
        <button type="button" disabled={activePage === 1} onClick={() => setActivePage(1)}>
          ⏮️ First
        </button>
        <button type="button" disabled={activePage === 1} onClick={() => setActivePage(activePage - 1)}>
          ⬅️ Previous
        </button>
        <button type="button" disabled={activePage === totalPages} onClick={() => setActivePage(activePage + 1)}>
          Next ➡️
        </button>
        <button type="button" disabled={activePage === totalPages} onClick={() => setActivePage(totalPages)}>
          Last ⏭️
        </button>
      </div>
      <p>
        Page {activePage} of {totalPages} - Rows: {beginning === end ? end : `${beginning} - ${end}`} of {totalItems}
      </p>
    </>
  );
}

Pagination.propTypes = {
  activePage: PropTypes.number.isRequired,
  totalItems: PropTypes.number.isRequired,
  rowsPerPage: PropTypes.number.isRequired,
  setActivePage: PropTypes.func.isRequired,
};

export default Pagination;
