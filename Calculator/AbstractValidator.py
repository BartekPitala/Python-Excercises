import abc

class AbstractValidator:

    @abc.abstractmethod
    def validate(self, arg1, arg2):
        """validation..."""