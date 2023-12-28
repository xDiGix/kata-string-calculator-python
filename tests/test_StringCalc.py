from unittest import TestCase
from src.StringCalc import StringCalc

class TestStringCalc(TestCase):

    def setup_method(self, method):
        self.string_calc = StringCalc()

    def test_sum_empty_string(self):
        self.assertEqual(self.string_calc.add(''), 0)

    def test_sum_one_string(self):
        self.assertEqual(self.string_calc.add('1'), 1)

    def test_sum_two_string(self):
        self.assertEqual(self.string_calc.add('1,2'), 3)

    def test_sum_three_string(self):
        self.assertEqual(self.string_calc.add('3,5,1'), 9)

    def test_sum_with_different_delimiters_string(self):
        self.assertEqual(self.string_calc.add('1\n2,3'), 6)

    def test_sum_with_custom_delimiters_string(self):
        self.assertEqual(self.string_calc.add('//;\n1;2'), 3)

    def test_sum_with_negative_string(self):
        with self.assertRaises(Exception) as context:
            self.string_calc.add('-1')

        self.assertTrue('Negatives not allowed: -1' in str(context.exception))