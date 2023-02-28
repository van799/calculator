from core.calculator import Calculator
from config.config_project import logger

#Rename!
class BaseCalculator(Calculator):
    #why you need log this?
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
    #Rename -> calculate verb
    def calculator(self, operations, a, b):
        if operations == '+':
            result = BaseCalculator.add(a, b)
            logger.debug(f"Class: calculator method: operation add. a = '{a}', b = '{b}', result = '{result}'")
            #remove self.complete
            self.complete
            return result

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

# 1 Errors
# 2 Input data, output and results
# 3 Specific cases: external calls ant etc