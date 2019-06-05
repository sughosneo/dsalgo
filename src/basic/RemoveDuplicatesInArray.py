'''
    This below script shows the methodlogy to remove duplicates from a arraylist
    In this sctipt we actually mentioned about 2 of the approaches.

    1. Using Dict/HashMap
    2. Using sorting mechanism

'''

# Total avg complexity would be O(n) + o(m)
def removeDuplicatesUsingDict(inputArr):

    modifiedArrayList = []
    duplicateDict = {}

    # Time complexity of this loop O(n) * O(1)
    # If the insertion in the Linked List takes order of O(n)
    for eachElement in inputArr:
        if eachElement in duplicateDict :
            duplicateDict[eachElement] = duplicateDict[eachElement] + 1
        else:
            duplicateDict[eachElement] = 1

    # Time complexity of this loop O(n)
    for key,value in duplicateDict.items():

        modifiedArrayList.append(key)

    return modifiedArrayList


# Total time complexity would be - O(nlogn) + O(n)
def removeDuplicatesUsingSorting(inputArrList):

    modifiedArrList = []

    # Time complexity would be - O(nlogn)
    inputArrList = sorted(inputArrList)

    print(inputArrList)

    previousElement = -111

    # Time complexity would be - O(n)
    for index in range(0,len(inputArrList)):

        currentItem = inputArrList[index]

        if previousElement == currentItem:
            continue
        else:
            modifiedArrList.append(currentItem)

        previousElement = currentItem


    return modifiedArrList

if __name__ == '__main__':

    inputArr = [3,8,2,12,20,2,8]
    #inputArr = [3, 8, 2, 12, 20, 1, 8]

    #modifiedArrList = removeDuplicatesUsingDict(inputArr)

    modifiedArrList = removeDuplicatesUsingSorting(inputArr)

    print(modifiedArrList)


