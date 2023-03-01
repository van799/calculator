from core.input_data_base import InputDataBase


class InputData(InputDataBase):
    def __init__(self, input_data_math):
        self.date_split_operation = ''
        self.__input_data_math = input_data_math

    def parse_data(self, ):
        list_operation = ['+', '-', '*', '/']
        for operation in list_operation:
            self.__input_data_math = self.__input_data_math.replace(
                operation, f' {operation} '
            )
        return self.__input_data_math.split()
