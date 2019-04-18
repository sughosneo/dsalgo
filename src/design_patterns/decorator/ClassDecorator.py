'''

    This script shows the example of class based decorator types.

'''

import time

''' This is the decorator with class and with bool True/False decorator argument, which would control will control execution '''
class TimeFuncClassBasedDecorator:

    func_to_decorate = None

    def __init__(self,func_to_decorate):
        self.func_to_decorate = func_to_decorate

    def __call__(self,*args, **kwargs):

        startTime = time.time()

        self.func_to_decorate(*args)

        endTime = time.time()

        executionTime = endTime - startTime

        print("Total time taken in : ", self.func_to_decorate.__name__, executionTime)


''' This is the decorator with class and with bool True/False decorator argument, which would control will control execution '''
class TimeFuncClassBasedDecoratorWithArgument:

    isRequired = None

    def __init__(self,isRequired):

        self.isRequired = isRequired

    def __call__(self,func_to_decorate,*args, **kwargs):

        def decoratedfunc(*args, **kwargs):

            if self.isRequired:

                startTime = time.time()

                func_to_decorate(*args)

                endTime = time.time()

                executionTime = endTime - startTime

                print("Total time taken in : ", func_to_decorate.__name__, executionTime)

            else:

                func_to_decorate(*args)
                print("Execution complete ", func_to_decorate.__name__)

        return decoratedfunc