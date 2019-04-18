'''
    Ref : http://scottlobdell.me/2015/04/decorators-arguments-python/
'''
import time
from FuncDecorator import doTimeFuncExecutionDecorator,doTimeFuncExecutionDecoratorWithArgument
from ClassDecorator import TimeFuncClassBasedDecorator,TimeFuncClassBasedDecoratorWithArgument

####################
## Below block shows - function decorator example
##################################################
@doTimeFuncExecutionDecorator
def delay():
    time.sleep(5)

@doTimeFuncExecutionDecoratorWithArgument(False)
def furtherDelay():
    time.sleep(5)
#######################################################

####################
## Below block shows example of class type decorator
##################################################
@TimeFuncClassBasedDecorator
def delayExecution(executionTimeInSecs):
    time.sleep(executionTimeInSecs)

@TimeFuncClassBasedDecoratorWithArgument(False)
def furtherDelayExecution():
    time.sleep(5)
#######################################################


if __name__ == '__main__':

    #region - Function type decorator

    # This is method call with a decorator with no argument.
    delay()

    # This is method call with a decorator with bool True/False argument.
    furtherDelay()

    #endregion

    #region - Class type decorator

    # This is the class decorator without any argument
    delayExecution(5)

    # This is the class decorator with bool argument.
    furtherDelayExecution()

    #endregion
