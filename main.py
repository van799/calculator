from config.config_project import logger
from implementation.base_calculator import BaseCalculator

base_calculator = BaseCalculator()

try:
    a = input("Введите первое число:")
    b = input("Введите второе число:")
    operation = input("Введите операцию:")
    logger.info('input data')
    print(base_calculator.calculator(operation, int(a), int(b)))
except ValueError:
    logger.warning(f'input data warning {a}, {b}, {operation}')
