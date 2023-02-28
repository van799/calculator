from abc import ABC, abstractmethod


class Calculator(ABC):
    def __init__(self):
        self.__complete = False

    @abstractmethod
    def calculator(self):
        pass

    @property
    def complete(self):
        return self.__complete
