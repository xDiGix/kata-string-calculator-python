from unittest import TestCase
from src.StringCalc import StringCalc

class TestStringCalc(TestCase):

    def setup_method(self, method):
        self.string_calc = StringCalc()

    def test_empty_string(self):
        self.assertEqual(self.string_calc.add(''), 0)