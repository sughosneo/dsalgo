from abc import ABC, abstractmethod

class AbstractPublisher(ABC):


    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def notify(self):
        pass

