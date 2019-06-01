'''
    Below is the implementation of Heap data structure.
    Standard operation has been captured.
    Sample example has been provided in here -
'''

class Heap:

    __heapList = None
    __heapSize = None

    def __init__(self):
        self.__heapList = [0]
        self.__heapSize = 0

    '''
        Below method would actually insert individual item in the array.
        Then heapify method would actually keep the heap structure. 
    '''
    def insert(self,item):

        if item:

            self.__heapList.append(item)
            self.__heapSize = self.__heapSize + 1
            self.heapify(self.__heapSize)

    '''
        Below method would actually to keep the structure of the heap property.
    '''
    def heapify(self,index):

        print(self.__heapList)
        print(index,index // 2)
        while index // 2 > 0:

            if self.__heapList[index] < self.__heapList[index // 2]:
                tmp = self.__heapList[index // 2]
                self.__heapList[index // 2] = self.__heapList[index]
                self.__heapList[index] = tmp

            index = index // 2

    def getTotalitems(self):

        return self.__heapSize

    def printHeapItems(self):

        print(self.__heapList)

    def delMin(self,itemValue):
        pass

if __name__ == '__main__':

    heap = Heap()
    itemList = [5,9,11,14,18,19,21,33,17,27]
    #itemList = [1, 9, 8, 2]

    for eachItem in itemList:
        heap.insert(eachItem)

    print("---------------")
    print(heap.getTotalitems())

    print("---------------")
    heap.printHeapItems()