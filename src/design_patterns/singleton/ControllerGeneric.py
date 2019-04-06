from SingletonGeneric import *

@Singleton
class ControllerGeneric:

    def __init__(self,value):
        print("It has been initialized")

    def geInfo(self):
        print("Get information")


if __name__ == '__main__':

    controllerOne = ControllerGeneric(5)
    print("Here is the first obj memory reference")
    print(id(controllerOne))

    print("Here is the second obj memory reference")
    controllerTwo = ControllerGeneric(10)
    print(id(controllerTwo))


