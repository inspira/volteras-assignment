const Table = ({ columns, rows }) => {
  return (
    <table>
      <thead>
        <tr>
          {columns.map(column => {
            return <th key={column.accessor}>{column.label}</th>
          })}
        </tr>
      </thead>
      <tbody>
        {rows.map(row => {
          return (
            <tr key={row.id}>
              {columns.map(column => {
                if (column.format) {
                  return <td key={column.accessor}>{column.format(row[column.accessor])}</td>
                }
                return <td key={column.accessor}>{row[column.accessor]}</td>
              })}
            </tr>
          )
        })}
      </tbody>
    </table>
  )
}

export default Table;
