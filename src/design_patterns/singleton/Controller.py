from Singleton import *

if __name__ == '__main__':

    singletonObjOne = Singleton.instance()
    print("Memory address of the first obj")
    print(id(singletonObjOne))

    singletonObjOne = Singleton.instance()
    print("Memory address of the second obj")
    print(id(singletonObjOne))

    print("Can I initiate the object")
    singletonObjThree = Singleton()
    print(singletonObjThree)




