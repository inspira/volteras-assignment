#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This python script reads the sample csv files in the `sample_data` dir
and executes a POST request to the `vehicle_data` API for each data point
"""

import csv
import logging
import pathlib
import sys
import requests

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

API_BASE_URI = sys.argv[1]
if not API_BASE_URI:
    log.error('Please provide the API base URI (e.g: http://localhost:8000)')

API_URI: str = f'{API_BASE_URI}/api/v1/vehicle_data/'

response = requests.get(API_URI)
if response.status_code == 200 and len(response.json()) > 1:
    log.info('Data already loaded. Exiting')
    sys.exit()

log.info('Starting import')

for filepath in (
    pathlib.Path(__file__).parent.joinpath(
        '../sample_data').resolve().glob('*.csv')
):
    vehicle_id = filepath.stem
    log.info('Loading sample data for vehicle %s', vehicle_id)
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            entry = {'vehicle_id': vehicle_id, **line}
            res = requests.post(
                API_URI, json=entry, timeout=10)
            log.info('Data successfully loaded: %s', res)
            if res.status_code != 201:
                log.error('Error loading entry: %s', entry)
                log.error('Response code: %s', res.status_code)

log.info('Import complete')
