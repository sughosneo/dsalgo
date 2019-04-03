'''
    This is controller class which would decide the publisher and subscriber flow.
'''
from Publisher import *
from SubscriberOne import *
from SubscriberTwo import *

if __name__ == '__main__':

    pub = Publisher()

    subOne = SubscriberOne()
    subTwo = SubscriberTwo()

    pub.attach(subOne)
    pub.attach(subTwo)

    print("All subscribers are notified")

    pub.notify()

    pub.detach(subOne)

    print("Again subscribers are being notified")

    pub.notify()
