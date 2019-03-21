''''

    This the stack implementation using singly linked list.
    Sample data does like below :

    H -> Next
    9 -> 10 -> 18 -> 7 -> 11 -> 5

    Where self.__topItem = 9

'''
class Node:

    value = None       # This would hold the value of the individual node item.
    next = None       # Child also represent

    def __init__(self,value):

        self.value = value
        self.next = None


class Stack:

    __topItem = None    # Top item is nothing but the last item in the linked list.
    __noOfElements = 0

    def __init__(self):
        self.__topItem = None

    def getTopItem(self):

        return self.__topItem

    def pop(self):

        if self.__topItem :

            currentNode = self.__topItem
            self.__topItem = currentNode.next

            self.__noOfElements = self.__noOfElements - 1

            return 1

        else :

            return -1

    def push(self,newNode):

        # That means provided newNode is not None
        if newNode and newNode.value:

            if self.__topItem is None:
                self.__topItem = newNode
                self.__noOfElements = self.__noOfElements + 1

            else:

                newNode.next = self.__topItem                   # Point the new item next item to the old top item.
                self.__topItem = newNode                        # Move the pointer to last.
                self.__noOfElements = self.__noOfElements + 1

                return 1

        else:
            return -1

    def sizeOfStack(self):
        return self.__noOfElements

if __name__ == '__main__':

    customStack = Stack()


    #region // Add values to the stack
    node = Node(5)
    customStack.push(node)

    node = Node(11)
    customStack.push(node)

    node = Node(7)
    customStack.push(node)

    node = Node(18)
    customStack.push(node)

    node = Node(10)
    customStack.push(node)

    node = Node(9)
    customStack.push(node)

    #endregion


    topItem = customStack.getTopItem()
    print("Top Item", topItem.value)


    #region // Pop Item
    customStack.pop()
    topItem = customStack.getTopItem()
    print("Top Item", topItem.value)

    #endregion