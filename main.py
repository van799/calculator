from implementation.input_data import InputData
from implementation.validate_data import ValidateData


input_data = InputData('10 + 2- 654+6/9+ 10.5')
validate_data = ValidateData(input_data.parse_data())

print(validate_data)
