'''

        Below is the generic implementation of
'''
def Singleton(cls):

    __instances = {}

    def getInstance(*args,**kwargs):

        if cls not in __instances:
            __instances[cls] = cls(*args,**kwargs)
            print(*args)
        return __instances[cls]

    return getInstance