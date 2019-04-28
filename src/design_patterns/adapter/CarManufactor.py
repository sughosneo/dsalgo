import abc
from BMWManufactor import *

class CarManufactor(metaclass=abc.ABCMeta):

    def __init__(self):

        self._adaptee = BMWManufactor()

    @abc.abstractmethod
    def manufactoring(self):
        pass
