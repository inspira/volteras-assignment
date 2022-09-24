# Volteras Take-at-home Challenge - Backend

This is the FastAPI app for the Take-at-home Challenge as proposed by Volteras.

## How to execute

### Docker

The easiest way to setup the backend is by running it using Docker:
```
docker-compose up --build -d
```
This command will:

- Set up a PostgreSQL database container
- Build and run the API
- Load the sample CSV data into the database through the API

### Python / Uvicorn

If you prefer to run the app outside docker, you will need to bring your own database and change the connection string accordingly, by editing `api/.env`. After this step, run the following commands to start the API server:
```
cd api
pipenv install --dev
pipenv run uvicorn main:app --reload
```

You should be able to reach the API through the address http://localhost:8000/api/v1/vehicle_data

## Code validation
```
# From the backend/ dir:
pipenv install pre-commit
pipenv run pre-commit
```

A hook can be installed in order to automatically validate the code automatically for each new git commit:
```
pipenv run pre-commit install
```

## Running e2e tests

From docker:
```
docker exec -it backend-api-1 sh -c 'SQLALCHEMY_DATABASE_URL="postgresql+psycopg2://evdata:evdata@postgres:5432/evdata_e2e_test" pytest'
```

From python:
```
SQLALCHEMY_DATABASE_URL="postgresql+psycopg2://evdata:evdata@postgres:5433/evdata_e2e_test" pipenv run pytest
```

If you want to use sqlite instead:
```
SQLALCHEMY_DATABASE_URL="sqlite:////tmp/test.db" pipenv run pytest
```
