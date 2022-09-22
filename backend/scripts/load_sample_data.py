#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This python script reads the sample csv files in the `sample_data` dir
and executes a POST request to the `vehicle_data` API for each data point
"""

import csv
import logging
import pathlib
import requests

API_URI_PREFIX: str = 'http://localhost:8000/api/v1'

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
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
                f'{API_URI_PREFIX}/vehicle_data/', json=entry, timeout=10)
            log.info('Data successfully loaded: %s', res)
            if res.status_code != 201:
                log.error('Error loading entry: %s', entry)
                log.error('Response code: %s', res.status_code)

log.info('Import complete')
