"""
Abstract repository - so we can use mocks in the unit tests
"""

from abc import ABC, abstractmethod

class Repository(ABC):
    """
    Abstract repository class
    """

    @abstractmethod
    # pylint: disable=too-many-arguments
    def list_vehicle_data_points(
        self,
        vehicle_id=None,
        from_timestamp=None,
        to_timestamp=None,
        sort_by=None,
        sort_order=None,
        page_size=None,
        page_index=None
    ):
        """
        Abstract method
        """

    @abstractmethod
    def get_vehicle_data_point(
        self,
        data_point_id: int
    ):
        """
        Retrieves a single data point for a vehicle
        """

    @abstractmethod
    def save_vehicle_data_point(
        self,
        entry
    ):
        """
        Saves a vehicle data point into the database
        """
