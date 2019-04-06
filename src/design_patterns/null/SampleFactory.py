from inspect import getmembers,isclass,isabstract
from ConcreteNullSample import *
import importlib

class SampleFactory:

    # __concreteSampleClasses = {}
    #
    # def __init__(self):
    #
    #     self.loadSampleConcreteClasses()
    #
    # def loadSampleConcreteClasses(self):
    #
    #     allClasses = getmembers(dsalgo.src.design_patterns.null,lambda m:isclass(m) and not isabstract(m))
    #     print(allClasses)
    #     for name,_type in allClasses:
    #         if isclass(_type) and issubclass(_type,dsalgo.src.design_patterns.null.AbstractSample):
    #             self.__concreteSampleClasses.update([[name,_type]])
    #
    #
    # def createInstance(self,className):
    #
    #     if className in self.__concreteSampleClasses:
    #         return self.__concreteSampleClasses[className]()
    #     else:
    #         return self.__concreteSampleClasses["ConcreteNullSample"]()

    def createInstance(self,className):

        try:

            module = importlib.import_module(className)
            class_ = getattr(module, className)
            instance = class_()

        except Exception as e:
            print(e)
            return ConcreteNullSample()

        return instance




