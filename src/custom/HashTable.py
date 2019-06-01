'''
    This is one of the simple hashing function.
    It could be any complicated hashing function as it gets.
'''
class HashingHelper:

    def getHashedValue(self,input):

        return input % 10

'''
    Below class would actually hold individual item.
    In the HashTable item we would always linked list item.
'''
class Node:

    key = None
    value = None       # This would hold the value of the individual node item.
    next = None        # Next is the reference of next node item.

    def __init__(self,key,value):

        self.key = key
        self.value = value
        self.next = None


'''
    This is the custom hash table implementation in python.
'''
class HashTable:

    __hashTable = None
    __noOfElements = None
    hashingHelper = None

    def __init__(self):

        self.__hashTable = []
        self.__noOfElements = 0

        self.hashingHelper = HashingHelper()

    '''
        This is the inserting function on Hash Table where 
            based on the hash index value. Value would get inserted in a list.
            If there is a collision then it would get inserted in a Linked List.
    '''
    def insert(self,key,value):

        if key :

            hashedIndexValue = self.hashingHelper.getHashedValue(key)

            if hashedIndexValue <= (len(self.__hashTable)-1) :

                # Hold new node.
                node = Node(key,value)

                lastNode = self.__hashTable[hashedIndexValue]
                currentNode = lastNode

                # Check the last of the current node.
                while(currentNode):

                    lastNode = currentNode
                    currentNode = currentNode.next

                # Add value
                lastNode.next = node

                self.__hashTable.append(node)

                self.__noOfElements = self.__noOfElements + 1

            elif hashedIndexValue > (len(self.__hashTable)-1):

                # Hold new node
                node = Node(key,value)

                self.__hashTable.append(node)

                self.__noOfElements = self.__noOfElements + 1

        else:
            raise ValueError("Key value is None")

    '''
        This method would actually return the value based on the hash table key.
    '''
    def getValue(self,key):

        value = None

        hashedIndexValue = self.hashingHelper.getHashedValue(key)

        if hashedIndexValue <= (len(self.__hashTable) -1):

            lastNode = self.__hashTable[hashedIndexValue]

            if lastNode :

                currentNode = lastNode

                if currentNode.key == key:
                    value = currentNode.value

                else:

                    while(currentNode):

                        if (currentNode.key == key):
                            value = currentNode.value
                            break

                        lastNode = currentNode
                        currentNode = currentNode.next

                    # If value is still None
                    if value == None:
                        raise KeyError("Key not present in dict!")

            else:
                raise KeyError("Key not present in dict!")
        else:
            raise KeyError("Key not present in dict!")

        return value

    def delete(self,key):

        hashedIndexValue = self.hashingHelper.getHashedValue(key)

        if hashedIndexValue <= (len(self.__hashTable) - 1):

            lastNode = self.__hashTable[hashedIndexValue]

            if lastNode:

                currentNode = lastNode

                if currentNode.key == key:
                    self.__hashTable[hashedIndexValue] = None
                    self.__noOfElements = self.__noOfElements - 1

                else:

                    while (currentNode):

                        lastNode = currentNode

                        if currentNode.next :

                            nextNode = currentNode.next

                            if (nextNode.key == key):

                                lastNode.next = nextNode.next
                                self.__noOfElements = self.__noOfElements - 1

                        currentNode = currentNode.next

            else:
                raise KeyError("Key not present in dict!")
        else:
            raise KeyError("Key not present in dict!")

    def getCount(self):

        return self.__noOfElements

if __name__ == '__main__':

    hashTable = HashTable()

    print("---Inserting key values in the Hash table ---")
    hashTable.insert(10,"Cat")
    hashTable.insert(11, "Bat")
    hashTable.insert(22, "Rat")
    hashTable.insert(32, "Sat")
    hashTable.insert(42, "Hat")

    print("---Total Number of Items---")
    print(hashTable.getCount())

    print("---Get specific value from Hash Table based on Key---")
    print(hashTable.getValue(32))

    print("---Delete Key from the Hash Table ---")
    print(hashTable.delete(32))

    print("---Retrive Key from the Hash Table ---")
    print(hashTable.getValue(42))

    print("---Total Number of Items---")
    print(hashTable.getCount())

    print("---Retrive Key from the Hash Table ---")
    print(hashTable.getValue(32))
