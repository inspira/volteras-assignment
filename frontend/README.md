# Volteras Take-at-home Challenge - Frontend

This is the React app for the Take-at-home Challenge as proposed by Volteras.

## How to execute
```
npm install
npm start
```

You should be able to see a page with the "Volteras Vehicle Data" table by accessing http://localhost:3000.

If you see the error message `Failed to load data: TypeError: Failed to fetch`, then either the backend API server is not started or it can't be reached by the frontend.

## Code validation

```
# From the frontend/ dir:
npx eslint src --ext .jsx --fix
```

TODO: run it as a git commit hook
