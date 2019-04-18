import time


def doTimeFuncExecutionDecorator(func_to_decorate):

    ''' Decorators with functions '''

    def timeFuncExec(*args,**kwargs):

        startTime = time.time()

        func_to_decorate(*args, **kwargs)

        endTime = time.time()

        executionTime = endTime - startTime

        print("Total time taken in : ", func_to_decorate.__name__, executionTime)

    return timeFuncExec

def doTimeFuncExecutionDecoratorWithArgument(isRequired):

    ''' Decorators with arguments '''

    def doTimeFuncExecutionDecorator(func_to_decorate):

        ''' Decorators with functions '''

        def timeFuncExec(*args,**kwargs):

            if isRequired :

                startTime = time.time()

                func_to_decorate(*args,**kwargs)

                endTime = time.time()

                executionTime = endTime - startTime

                print("Total time taken in : ", func_to_decorate.__name__,executionTime)

            else:
                func_to_decorate(*args,**kwargs)
                print("Execution complete ", func_to_decorate.__name__)

        return timeFuncExec

    return doTimeFuncExecutionDecorator





