'''
    This is the client side code of Null pattern.
    As we have null paettern has been declared so we don't need to check if instance variable is None or not.
    That's the advantage of using Null pattern.
'''

from SampleFactory import *

if __name__ == '__main__':

    sampleFactory = SampleFactory()

    for _className in ["ConcreteSampleOne","ConcreteSampleTwo","ConcreteSampleThree"]:
        instance = sampleFactory.createInstance(_className)
        print(instance.doSomething())


