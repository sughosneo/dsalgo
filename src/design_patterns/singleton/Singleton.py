'''
    This is the class which would show Singleton implementations
'''
class Singleton:

    __instance = None

    @classmethod
    def instance(cls):

        if cls.__instance == None:
            cls.__instance = Singleton()
        return cls.__instance


    def __init__(self):

        if self.__instance !=None:
            raise ValueError("Already an object exist!")



