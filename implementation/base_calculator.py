from core.calculator import Calculator
from config.config_project import logger


class BaseCalculator(Calculator):
    logger.info('get base calculator')

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def odd(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('division on zero')

    def calculator(self, operations, a, b):
        if operations == '+':
            logger.info('operation add')
            self.complete
            return BaseCalculator.add(a, b)

        elif operations == '-':
            logger.info('operation odd')
            self.complete
            return BaseCalculator.odd(a, b)

        elif operations == '*':
            logger.info('operation mult')
            self.complete
            return BaseCalculator.mul(a, b)

        elif operations == '/':
            logger.info('operation div')
            self.complete
            return BaseCalculator.div(a, b)
        else:
            logger.debug('operation div')
            return None
