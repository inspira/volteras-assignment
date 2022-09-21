# Volteras Take-at-home Challenge - Backend

This is the FastAPI app for the Take-at-home Challenge as proposed by Volteras.

## How to execute

You will need a Postgres DB instance running. If you have docker, you can start a Postgres container by running:
```
docker-compose up -d
```

If you bring your own database, you will need to change the connection string accordingly, by editing `api/.env`

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
