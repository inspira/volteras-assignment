FROM python:3.10-slim

# Install requirements
RUN pip install --no-cache-dir pipenv

WORKDIR /app

# Install requirements through pipenv
COPY Pipfile* ./
RUN pipenv install --system
RUN pipenv install uvicorn

# Run container as a non-root user for extra security
RUN adduser --system --no-create-home nonroot
USER nonroot

COPY api/logging.config.ini sample_data/ scripts/load_sample_data.py ./

EXPOSE 3000

HEALTHCHECK --interval=5m --timeout=3s \
 CMD curl https://localhost:8000/health -k || exit 1

CMD uvicorn evdata.main:app \
    --host 0.0.0.0 \
    --port 3000 \
    --log-config logging.config.ini
