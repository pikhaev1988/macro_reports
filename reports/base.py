from abc import ABC, abstractmethod


class BaseReport(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def generate(self):
        pass
