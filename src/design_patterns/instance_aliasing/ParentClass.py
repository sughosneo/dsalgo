from ChildClass1 import *
from ChildClass2 import *

class ParentClass:

    __version = "V1"
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):

        if cls.__version == "V1":
            cls.__instance = ChildClass1()
        elif cls.__version == "V2":
            cls.__instance = ChildClass2()
        else:
            raise ValueError("Version is not available!")

        return cls.__instance