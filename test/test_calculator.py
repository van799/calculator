import unittest
from implementation.base_calculator import BaseCalculator


class TestBaseCalculator(unittest.TestCase):

    def test_operation_add(self):
        a = 5
        b = 10
        test_calc = a + b
        base_calc = BaseCalculator()
        test_result = base_calc.calculator('+', a, b)
        self.assertEqual(test_result, test_calc)

    def test_operation_odd(self):
        a = 5
        b = 10
        test_calc = a - b
        base_calc = BaseCalculator()
        test_result = base_calc.calculator('-', a, b)
        self.assertEqual(test_result, test_calc)

    def test_operation_mul(self):
        a = 5
        b = 10
        test_calc = a * b
        base_calc = BaseCalculator()
        test_result = base_calc.calculator('*', a, b)
        self.assertEqual(test_result, test_calc)

    def test_operation_div_b_is_not_equal_to_zero(self):
        a = 5
        b = 10
        test_calc = a / b
        base_calc = BaseCalculator()
        test_result = base_calc.calculator('/', a, b)
        self.assertEqual(test_result, test_calc)

    def test_operation_div_b_to_zero(self):
        a = 5
        b = 0
        base_calc = BaseCalculator()
        base_calc.calculator('/', a, b)
        self.assertRaises(ZeroDivisionError)

    def test_unknown_operation(self):
        a = 5
        b = 0
        result_test = None
        base_calc = BaseCalculator()
        result = base_calc.calculator('=', a, b)
        self.assertEqual(result, result_test)
