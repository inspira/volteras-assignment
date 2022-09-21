#!/usr/bin/env python

import csv
import logging
import pathlib
import requests

API_URL: str = "http://localhost:8000/api/v1"

"""
This python script reads the sample csv files in the `sample_data` dir
and executes a POST request to the `vehicle_data` API for each data point
"""
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.info("Starting import")

for filepath in (
    pathlib.Path(__file__).parent.joinpath("../sample_data").resolve().glob("*.csv")
):
    vehicle_id = filepath.stem
    log.info(f"Loading sample data for vehicle {vehicle_id}...")
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            entry = {"vehicle_id": vehicle_id, **line}
            res = requests.post(f"{API_URL}/vehicle_data/", json=entry)
            log.info(f"Data successfully loaded: {res}")
            if res.status_code != 201:
                log.error(f"Error loading entry: {entry}")
                log.error(f"Response code: {res.status_code}")

log.info("Import complete")
