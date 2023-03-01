from abc import ABC, abstractmethod

#Rename abstarct class Calculator to CalculatorBase
#Don't methods and properties when you no needs them
class CalculatorBase(ABC):
    def __init__(self, validator, converter, output):
        self.__complete = False
        self.__validator = validator
        self.__output = output

    def _validate(self, a):
        return self._validate(a)

    def _print_result(self, result):
        output.Print(result)

    def _print_error(self, error_message):
        output.print_error(error_message)

    @abstractmethod
    def calculator(self):
        pass

    @property
    def complete(self):
        return self.__complete


#   Validation
#
#
#
#