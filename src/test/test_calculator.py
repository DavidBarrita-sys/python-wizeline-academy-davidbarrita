from src.main import functions_calculator as calculator
import unittest


class TestCalculator(unittest.TestCase):
    # This test case show if works addition function
    def test_case_addition(self):
        values = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        expected = 100
        actual = calculator.addition(values)
        self.assertEqual(actual, expected)

    def test_case_subtract_by_simple(self):
        values = [10, 3]
        expected = 7
        actual = calculator.subtract_by_simple(values)
        self.assertEqual(actual, expected)

    def test_case_subtract_by_target(self):
        values = [10, 3, 2, 1, 1]
        expected = 3
        actual = calculator.subtract_by_target(values)
        self.assertEqual(actual, expected)

    def test_case_multiplication_by_simple(self):
        values = [3000, 5]
        expected = 15000
        actual = calculator.multiplication_by_simple(values)
        self.assertEqual(actual, expected)

    def test_case_multiplication_by_n_values(self):
        values = [100, 100, 100]
        expected = 1000000
        actual = calculator.multiplication_by_n_values(values)
        self.assertEqual(actual, expected)

    def test_case_divide_by_simple(self):
        values = [10, 2]
        expected = 5
        actual = calculator.divide_by_simple(values)
        self.assertEqual(actual, expected)

    def test_case_root_by_n_values(self):
        values = [4, 8, 12]
        expected = [2, 2.8284271247461903, 3.4641016151377544]
        actual = calculator.root_by_n_values(values)
        self.assertEqual(actual, expected)

    def test_case_root_by_simple(self):
        values = [124]
        expected = 11.135528725660043
        actual = calculator.root_by_simple(values)
        self.assertEqual(actual, expected)

    def test_case_pow_by_simple(self):
        values = [3, 10]
        expected = 59049
        actual = calculator.pow_by_simple(values)
        self.assertEqual(actual, expected)

    def test_case_sin_by_simple(self):
        values = [3]
        expected = [0.1411200080598672]
        actual = calculator.sin_by_simple(values)
        self.assertEqual(actual, expected)

    def test_case_sin_by_n_values(self):
        values = [4, 8]
        expected = [-0.7568024953079282, 0.9893582466233818]
        actual = calculator.sin_by_n_values(values)
        self.assertEqual(actual, expected)

    def test_case_cos_by_simple(self):
        values = [1]
        expected = [0.5403023058681398]
        actual = calculator.cos_by_simple(values)
        self.assertEqual(actual, expected)

    def test_case_cos_by_n_values(self):
        values = [4, 8]
        expected = [-0.6536436208636119, -0.14550003380861354]
        actual = calculator.cos_by_n_values(values)
        self.assertEqual(actual, expected)

    def test_case_tan_by_simple(self):
        values = [4]
        expected = [1.1578212823495777]
        actual = calculator.tan_by_simple(values)
        self.assertEqual(actual, expected)

    def test_case_tan_by_n_values(self):
        values = [12, 15]
        expected = [-0.6358599286615808, -0.8559934009085188]
        actual = calculator.tan_by_n_values(values)
        self.assertEqual(actual, expected)
