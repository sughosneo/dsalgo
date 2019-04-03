'''
    Concrete subscriber Two
'''

from AbstractSubscriber import AbstractSubscriber

class SubscriberTwo(AbstractSubscriber):

    def update(self):

        print("Subscriber Two - has been updated !")
