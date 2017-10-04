import AbstractCalc
import math
from Validator import Validator
from sympy import diff


class Calc(AbstractCalc.AbstractCalc):

    oper = "None"

    def add(self, a , b):
        oper = "+"
        validator = Validator()
        validator.validate(a, b, oper)
        return a + b

    def log10(self, value):
        oper = "log"
        validator = Validator()
        validator.validate(value, 0 ,  oper)
        return math.log10(value)

    def divide(self, a, b):
        oper = "/"
        validator = Validator()
        validator.validate(a, b, oper)
        return a/b

    def derivate(self,fcn):
        oper = "der"
        validator = Validator()
        validator.validate(fcn, 0, oper)
        return diff(fcn)

