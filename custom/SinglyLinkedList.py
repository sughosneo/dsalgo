'''

    This is the singly linked list implementation in python.
    Node class hold the value and reference of the next item object.
    Representation is as per below :

    H                      		T
    5 -> 11 -> 7 -> 18 -> 10 -> 9

'''

class Node:

    value = None       # This would hold the value of the individual node item.
    next = None        # Next is the reference of next node item.

    def __init__(self,value):

        self.value = value
        self.next = None


'''
    This class holds all the operation related to one Singly Linked List.
'''
class SinglyLinkedList:

    __head = None
    __tail = None
    __noOfItems = None

    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__noOfItems = 0

    '''
        Method to insert single node in the linked list
    '''
    def insert(self,newNode):

        # If the new node value is not None and it has some value.
        if newNode and newNode.value :

            # If it's the very first item to be inserted.
            #    then in that scenario Head value would be None.
            if self.__head is None:
                self.__head = newNode
                self.__tail = self.__head

                self.__noOfItems = self.__noOfItems + 1         # Increase the item count.

                return 1

            else:

                self.__tail.next = newNode                       # Keep on increasing the __tail item one by one.
                self.__tail = newNode

                self.__noOfItems = self.__noOfItems + 1

                return 1

        else:
            return -1

    '''
        Delete one specific item
    '''
    def delete(self,itemValue):

        if itemValue :

            # If the item value is head value. This operation could be done in O(1)
            # So need to change the head value pointer.
            if itemValue == self.__head.value:
               headNextValue = self.__head.next
               self.__head = headNextValue
               self.__noOfItems = self.__noOfItems - 1 # Update the total item count.

            # This can't be done in O(1). You need to traverse the entire list.
            else :

                currnetNode = self.__head
                prevItem = None
                foundItem = None

                # Continue the loop until current node next value is not null.
                #       that means reach till the tail.
                while(currnetNode):

                    if currnetNode.value == itemValue:
                        foundItem = currnetNode
                        break
                    prevItem = currnetNode          # This would always keep holding on the previous item obj reference.
                    currnetNode = currnetNode.next

                # Means you have found the value in linked list.
                if foundItem :
                    prevItem.next = foundItem.next

                    #As this found item could be the tail item as well.
                    # So to keep track of the __tail item we would do require to do one extra check
                    # Here we are checking if the found item and tail items are same or not.
                    if foundItem == self.__tail:
                        self.__tail = prevItem

                    self.__noOfItems = self.__noOfItems - 1 # Update the no of items counter.
                    return 1
                else:
                    return -1

    '''
        Return Head node.
    '''
    def getHeadElement(self):
        return self.__head

    '''
        Return tail node.
    '''
    def getTailItem(self):
        return self.__tail

    '''
        Return total count of all the items in the present linked list.
    '''
    def getTotalItems(self):

        return self.__noOfItems

    '''
        Print all items in the present linked list.
    '''
    def printAllItems(self):

        currentItem = self.__head

        # Starting item head to run this loop till the last item.
        #       because after the last element we would find one None type.

        while(currentItem):
            print(currentItem.value)
            currentItem = currentItem.next

if __name__ == '__main__':

    linkedList = SinglyLinkedList()

    #region //Linked list insertion section
    node = Node(5)
    linkedList.insert(node)

    node = Node(11)
    linkedList.insert(node)

    node = Node(7)
    linkedList.insert(node)

    node = Node(18)
    linkedList.insert(node)

    node = Node(10)
    linkedList.insert(node)

    node = Node(9)
    linkedList.insert(node)
    #endregion

    #region // Print all items in linked list
    linkedList.printAllItems()
    #endregion

    #region // Find the head & Tail item
    headItem = linkedList.getHeadElement()
    print("Head Item", headItem.value)

    tailItem = linkedList.getTailItem()
    print("Tail Item", tailItem.value)
    #endregion

    #region // Delete one item

    itemValue = 9
    linkedList.delete(itemValue)
    linkedList.printAllItems()

    # Checking corner scenario - deleting tail item. It works for the middle item too.
    itemValue = 7
    linkedList.delete(itemValue)
    linkedList.printAllItems()

    #endregion

    # region // Find the head & Tail item
    headItem = linkedList.getHeadElement()
    print("Again Head Item", headItem.value)

    tailItem = linkedList.getTailItem()
    print("Again Tail Item", tailItem.value)
    # endregion













