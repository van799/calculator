from config.config_project import logger
from implementation.base_calculator import BaseCalculator

#Naming. The word base in the name of class means that class is abstract. Fix: rename class
base_calculator = BaseCalculator()

#Dont use try...catch in this maner!!!
try:
    a = input("Введите первое число:")
    b = input("Введите второе число:")
    operation = input("Введите операцию:")
    logger.info('input data')
    print(base_calculator.calculator(operation, int(a), int(b)))
except ValueError:
    logger.warning(f'input data warning {a}, {b}, {operation}')


#try:
#    risc_operation()
#except Known_Exception:
#    process catched exception


#command line arguments

# calculator.py 2+3
# 5