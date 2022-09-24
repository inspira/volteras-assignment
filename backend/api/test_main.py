# -*- coding: utf-8 -*-

"""
Sample E2E test
TODO: tests for paging, sorting and filtering
See: https://fastapi.tiangolo.com/tutorial/testing/
"""

from urllib.parse import urljoin
from fastapi.testclient import TestClient
from main import app


class TestMain:
    """
    This is a sample E2E test focused on how the API operations work together
    """

    client = TestClient(app)
    BASE_PATH = '/api/v1/vehicle_data/'
    VEHICLE_ID_1 = '7bcd5c8d-9d1a-57a1-0a1e-09ab10a8c1a0'
    VEHICLE_ID_2 = '9a987bd6-038e-a810-cd09-a0c9d87ef541'

    def test_health_check(self, _init_database):
        """
        Tests if the healthcheck works as expected
        """
        response = self.client.get("/health")
        assert response.status_code == 200
        assert response.json() == "OK"

    def test_post_data(self, _init_database):
        """
        Tests if a data entry is saved as expected
        """
        response = self.client.post(
            self.BASE_PATH,
            json={
                'elevation': 20,
                'odometer': 47686.8,
                'shift_state': 'D',
                'soc': 66,
                'speed': 20,
                'timestamp': '2022-07-12T20:11:54.149000',
                'vehicle_id': self.VEHICLE_ID_1,
            },
        )
        assert response.status_code == 201

    def test_read_data(self, _init_database):
        """
        Tests if the data entry saved in the test above is retrieved as expected
        """
        response = self.client.get(
            urljoin(self.BASE_PATH, f'?vehicle_id={self.VEHICLE_ID_1}')
        )
        response_data = response.json()['data']

        assert response.status_code == 200
        assert len(response_data) == 1

    def test_post_data_null_speed(self, _init_database):
        """
        Tests if a data entry with NULL values is saved as expected
        """
        response = self.client.post(
            self.BASE_PATH,
            json={
                'elevation': 20,
                'odometer': 47686.8,
                'shift_state': 'NULL',
                'soc': 66,
                'speed': 'NULL',
                'timestamp': '2022-07-12T20:11:54.149000',
                'vehicle_id': self.VEHICLE_ID_2,
            },
        )
        assert response.status_code == 201

    def test_read_data_null_speed(self, _init_database):
        """
        Tests if the data entry saved in the test above is retrieved as expected
        """
        response = self.client.get(
            urljoin(self.BASE_PATH, f'?vehicle_id={self.VEHICLE_ID_2}')
        )
        response_data = response.json()['data']
        first_item = response_data[0]

        assert response.status_code == 200
        assert len(response_data) == 1

        assert first_item['speed'] == 'NULL'
        assert first_item['shift_state'] == 'NULL'
