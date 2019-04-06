from abc import ABC,abstractmethod

class AbstractSample(ABC):

    @abstractmethod
    def doSomething(self):
        pass
        