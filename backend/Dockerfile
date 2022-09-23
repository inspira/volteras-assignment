# References:
# - https://sourcery.ai/blog/python-docker/
# - https://dev.to/mrpbennett/setting-up-docker-with-pipenv-3h1o
# - https://stackoverflow.com/questions/46503947/how-to-get-pipenv-running-in-docker



# Base image with sane env settings
FROM python:3.10-slim as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Displays helpful traceback information if a segfault occurs.
# See: https://stackoverflow.com/questions/21733856/python-is-there-a-downside-to-using-faulthandler
ENV PYTHONFAULTHANDLER 1

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1



# Temp image with apt/python/pip dependencies
FROM base AS python-deps

# Install pipenv
RUN pip install --no-cache-dir pipenv==2022.9.21 # no-cache-dir to make Docker images smaller

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .

# TODO: remove `--dev` when used in production
# See https://fastapi.tiangolo.com/deployment/manually/?h=uvicorn
# and https://fastapi.tiangolo.com/deployment/docker/?h=uvicorn#build-a-docker-image-for-fastapi
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --dev --deploy --ignore-pipfile



# Temp image with the virtualenv required for the runtime and the non-root user
# As well as the app code for execution
FROM base AS runtime

# Install curl for healthcheck and debug
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl=7.74.0-1.3+deb11u3 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user (for security reasons)
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY api/ ./api/
COPY sample_data/ ./sample_data/
COPY scripts/ ./scripts/



# Target image for the data import script
FROM runtime as import_data

CMD ["./scripts/load_sample_data.py", "http://api:8000"]



# Target image for the final app server
FROM runtime as app

EXPOSE 8000

HEALTHCHECK --interval=5m --timeout=5s \
 CMD curl http://127.0.0.1:8000/health -k || exit 1

WORKDIR /home/appuser/api/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
