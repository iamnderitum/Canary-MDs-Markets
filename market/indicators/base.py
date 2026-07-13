from abc import ABC
from abc import abstractmethod

class Indicator(ABC):

    @abstractmethod
    def calculate(self, dataframe):
        pass