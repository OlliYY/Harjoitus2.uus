from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def get_all(self):
        """Method to get all records"""
        pass
