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