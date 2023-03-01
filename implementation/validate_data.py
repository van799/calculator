from core.validate_data_base import ValidateDataBase


class ValidateData(ValidateDataBase):
    def __init__(self, data_class):
        self.data_class = data_class

    def validate(self):
        self.data_class
