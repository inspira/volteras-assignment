# Volteras Take-at-home Challenge

This is a solution for the Take-at-home Challenge as proposed by Volteras.

## Observations about the assessment

### General
- We've implemented most of the solution in 4 hours (until the [PR #4](https://github.com/thiagoalves/volteras-assignment/pull/4)). Paging, sorting and advanced filtering were implemented in approx. 2 hours more. 
  - Even with the extra 2 hours, we know there are still many opportunities for improvements. Some of them are mentioned  in this document and also in comments around the code.
- The code was reviewed internally by our team - some of the comments are in github, the other fixes were made during pair programming.
- We aimed at building a basic solution in short time (loading data to the database and displaying it on the browser), and from there on we added minor incremental fixes.
- Some of the files were created based on code templates we already had, which saved some time and took care of some non-functional requirements, such as security and maintainability:
  - `Dockerfile` / `docker-compose.yaml` / `.dockerignore`
  - Github Actions
  - Pre-commit hooks
- The documentation is split between general info on `README.md` files and self-documented / self-explanatory code


### Front-end
- There's a lot of space for improvement. We didn't add pagination or sorting during the first 4 hours, due to the time restrictions and this being a more time demanding activity than a complexity driven one. Improvements were added later based on [this post](https://www.taniarascia.com/front-end-tables-sort-filter-paginate/).
- We could consider using typescript rather than js

### Backend
- We put effort on code quality, security, standardization, and not just on functional requirements
- We could have used a time-series DB (perhaps DynamoDB and InfluxDB), but to keep it simple we opted for the relational DB with SQL Alchemy as described in the FastAPI docs.
  - Despite being relational, since it's a PostgreSQL DB it is easily adaptable (or even already compatible) to Redshift, which could handle huge amounts of data if required
- The CSV export functionality is pretty basic - we only added it because it took less than 5 min. Ideally we would make an API to generate other formats, and depending on the volume of data, using asynchronous queues

# General guidance

The solution is split into two parts:

- Backend ([documentation](backend/README.md))
- Frontend ([documentation](frontend/README.md))

The frontend is a React app. It makes REST API calls to the backend, which is a python 3 app based on FastAPI. The backend needs a PostgreSQL database in order to store the vehicle data points.

There is a docker-compose file for running the backend / database locally, in case you don't have PostgreSQL installed in your dev machine.
