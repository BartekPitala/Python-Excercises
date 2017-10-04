import AbstractValidator
from Exceptions import *


class Validator(AbstractValidator.AbstractValidator):

    def is_a_number(self, value):
        return isinstance(value, int) or isinstance(value, float)

    def is_a_string(self, value):
        return isinstance(value, str)

    def is_a_fcn(self, value):
        return callable(value)

    def is_zero(self, value):
        return value == 0

    def validate(self, a, b, operation):
        if operation == "+" and (not self.is_a_number(a) or not self.is_a_number((b))):
            raise NotANumber()

        if operation == "/" and (not self.is_a_number(a) or not self.is_a_number((b))):
            raise NotANumber()

        if operation == "/" and b == 0:
            raise DivideByZero()

        if not self.is_a_string(operation):
            raise NotAString()

        if not (operation == "+" or operation == "/" or operation == "log" or operation =="der"):
            raise WrongOperation()

        if operation == "log" and not self.is_a_number(a):
            raise WrongInput()

        if operation == "log" and a < 1:
            raise LowerThanOne()

        if operation == "der" and not self.is_a_string(a):
            raise NotAString
