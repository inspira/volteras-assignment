# Volteras Take-at-home Challenge - Frontend

This is the React app for the Take-at-home Challenge as proposed by Volteras.

## How to execute

Confirm that your node version is `16.17.0 LTS`

```
npm --version
```

Then install the dependencies and run the app

```
npm install
npm start
```

You should be able to see a page with the "Volteras Vehicle Data" table by accessing http://localhost:3000

If you see the error message `TypeError: Failed to fetch` on the top of the page, then either the backend API server is not started or it can't be reached by the frontend.

## Code validation

```
# From the frontend/ dir:
npx eslint src --ext .jsx --fix
```

TODO: run it as a git commit hook

## Table component

The `src/Table.jsx` component has been extracted from https://www.taniarascia.com/front-end-tables-sort-filter-paginate/
