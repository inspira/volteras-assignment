# -*- coding: utf-8 -*-

"""
Sample E2E test
"""

from urllib.parse import urljoin
import requests

# TODO: move to a config file
BASE_URL = 'http://localhost:3000/api/v1/vehicle_data/'


class SampleEndToEndTest:
    """
    This is a sample E2E test focused on how the API operations work together
    """
    @staticmethod
    def test_post_data():
        """
        Tests if a data entry is saved as expected
        """
        response = requests.post(
            BASE_URL,
            json={
                'elevation': 20,
                'odometer': 47686.8,
                'shift_state': 'D',
                'soc': 66,
                'speed': 20,
                'timestamp': '2022-07-12T20:11:54.149000',
                'vehicle_id': '1bbdf62b-4e52-48c4-8703-5a844d1da912',
            },
        )
        assert response.status_code == 201

    @staticmethod
    def test_read_data():
        """
        Tests if the data entry saved in the test above is retrieved as expected
        """
        response = requests.get(
            urljoin(BASE_URL, '1bbdf62b-4e52-48c4-8703-5a844d1da912')
        )
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data) == 1

    @staticmethod
    def test_post_data_null_speed():
        """
        Tests if a data entry with NULL values is saved as expected
        """
        response = requests.post(
            BASE_URL,
            json={
                'elevation': 20,
                'odometer': 47686.8,
                'shift_state': 'NULL',
                'soc': 66,
                'speed': 'NULL',
                'timestamp': '2022-07-12T20:11:54.149000',
                'vehicle_id': '06ab31a9-b35d-4e47-8e44-9c35feb1bfae',
            },
        )
        assert response.status_code == 201

    @staticmethod
    def test_read_data_null_speed():
        """
        Tests if the data entry saved in the test above is retrieved as expected
        """
        response = requests.get(
            urljoin(BASE_URL, '06ab31a9-b35d-4e47-8e44-9c35feb1bfae')
        )
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data) == 1
        assert response_data[0]['speed'] == 'NULL'
        assert response_data[0]['shift_state'] == 'NULL'
