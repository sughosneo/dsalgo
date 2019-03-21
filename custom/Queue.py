'''

    This is the custom Queue data structure implementation using singly linked list.
    Data flow has been considered as per representation :

Prev is none                   Prev is 11
 <- L							F
    9 <- 10 <- 18 <- 7 <- 11 <- 5

'''

class Node:

    value = None       # This would hold the value of the individual node item.
    prev = None       # Child also represent

    def __init__(self,value):

        self.value = value
        self.prev = None

class Queue:

    __first = None
    __last = None
    __totalNoOfElements = 0

    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self,newNode):

        if newNode and newNode.value :

            if self.__first  is None:

                self.__first = newNode
                self.__last  = self.__first
                self.__totalNoOfElements = self.__totalNoOfElements + 1

                return 1

            else:

                self.__last.prev = newNode
                self.__last = newNode

                self.__totalNoOfElements = self.__totalNoOfElements + 1

                return 1

        else:

            return -1

    def dqueue(self):

        if self.__first :

            previousNode = self.__first.prev
            self.__first = previousNode

            return 1
        else:
            return -1

    def getTotalNoOfElements(self):

        return self.__totalNoOfElements

    def getFirstElement(self):

        return self.__first

    def getLastElement(self):

        return self.__last

if __name__ == '__main__':

    q = Queue()

    #region // enqueue region
    node = Node(5)
    q.enqueue(node)

    node = Node(11)
    q.enqueue(node)

    node = Node(7)
    q.enqueue(node)

    node = Node(18)
    q.enqueue(node)

    node = Node(10)
    q.enqueue(node)

    node = Node(9)
    q.enqueue(node)
    #endregion

    firstElement = q.getFirstElement()
    print("Head Item", firstElement.value)

    q.dqueue()
    firstElement = q.getFirstElement()
    print("Head Item After DQueue Call", firstElement.value)
