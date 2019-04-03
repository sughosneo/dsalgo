from AbstractPublisher import AbstractPublisher

class Publisher(AbstractPublisher):

    __observerList = list()

    def __init__(self):
        pass

    def attach(self,observer):

        if observer:
            self.__observerList.append(observer)

    def detach(self,observer):

        if observer:
            self.__observerList.remove(observer)

    def notify(self):

        for eachObserver in self.__observerList :
            eachObserver.update()


