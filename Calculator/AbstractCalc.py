import abc

class AbstractCalc():

    @abc.abstractmethod
    def add(self , a , b):
        """add a to b"""

    @abc.abstractmethod
    def log10(self, value):
        """logarithm with a base of 10 from value"""

    @abc.abstractmethod
    def divide(self, a, b):
        """divide a by b"""

    @abc.abstractmethod
    def derivate(self, fcn):
        """count the derivative of fcn"""
