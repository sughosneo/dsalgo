from inspect import getmembers,isclass,isabstract
from ConcreteNullSample import *
import importlib

class SampleFactory:

    def createInstance(self,className):

        try:

            module = importlib.import_module(className)
            class_ = getattr(module, className)
            instance = class_()

        except Exception as e:
            print(e)
            return ConcreteNullSample()

        return instance




