import unittest
from Calc import Calc
from Exceptions import *
from mock import patch


class CalcTest(unittest.TestCase):

    def test_checking_addition_of_floats_returns_sum(self):
        calcul = Calc()
        a = 7.0
        b = 1.0
        suma = 8.0
        self.assertAlmostEqual(calcul.add(a, b), suma)

    def test_checking_addition_of_ints_returns_sum(self):
        calcul = Calc()
        a = 7
        b = 1
        suma = 8
        self.assertEqual(calcul.add(a, b) , suma)

    def test_checking_addition_of_int_and_str_raises_exception(self):
        calcul = Calc()
        a = 7
        b = "string"
        self.assertRaises(NotANumber, calcul.add, a, b)

    def test_checking_division_by_zero_raises_exception(self):
        calcul = Calc()
        a = 7
        b = 0
        self.assertRaises(DivideByZero, calcul.divide, a, b)

    def test_checking_division_of_int_and_string_raises_exception(self):
        calcul = Calc()
        a = "aaa"
        b = 12
        self.assertRaises(NotANumber, calcul.divide, a , b)

    def test_checking_division_of_two_floats_returns_correct_value(self):
            calcul = Calc()
            a = 2.0
            b = 4.0
            result = 0.5
            self.assertAlmostEqual(calcul.divide(a, b), result)

    def test_checking_division_of_two_strings_raises_exception(self):
        calcul = Calc()
        a = "string1"
        b = "string2"
        self.assertRaises(NotANumber, calcul.divide, a, b)

    def test_checking_log_of_float_returns_correct_value(self):
        calcul = Calc()
        a = 100.0
        log = 2
        self.assertAlmostEqual(calcul.log10(a), 2)

    def test_checking_log_of_string_raises_exception(self):
        calcul = Calc()
        a = "String"
        self.assertRaises(WrongInput, calcul.log10, a)

    def test_checking_log_of_value_smaller_than_one_raises_exception(self):
        calcul = Calc()
        a = 0.5
        self.assertRaises(LowerThanOne, calcul.log10, a)

    def test_checking_derivative_of_number_raises_exception(self):
        calcul = Calc()
        a = 7
        self.assertRaises(NotAString, calcul.derivate, a)

    def test_checking_derivative_of_string_fcn_returns_correct_value(self):
        calcul = Calc()



if __name__ == '__main__':
    unittest.main(exit=False)