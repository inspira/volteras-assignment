# References:
# - https://sourcery.ai/blog/python-docker/
# - https://dev.to/mrpbennett/setting-up-docker-with-pipenv-3h1o
# - https://stackoverflow.com/questions/46503947/how-to-get-pipenv-running-in-docker

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


FROM base AS python-deps

# Install pipenv
RUN pip install --no-cache-dir pipenv==2022.9.21 # no-cache-dir to make Docker images smaller

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --ignore-pipfile


FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Install required packages
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl=7.74.0-1.3+deb11u3 \
    && rm -rf /var/lib/apt/lists/*

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY api/ ./api/
COPY sample_data/ ./sample_data/
COPY scripts/ ./scripts/

RUN ls -la > ls.txt

EXPOSE 8000

HEALTHCHECK --interval=5m --timeout=5s \
 CMD curl http://127.0.0.1:8000/health -k || exit 1

WORKDIR /home/appuser/api/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
