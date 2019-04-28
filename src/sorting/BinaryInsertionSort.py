'''
    In the binary insertion sort we would require to find the location using binary search.
'''
def binarySearch(arrInput,itemToSearch):

    middleElementIndex = len(arrInput) // 2

    if itemToSearch == arrInput[middleElementIndex]:
        return middleElementIndex
    else:

        if len(arrInput) > 1:

            # Means if searchable item value is less than middle element.
            if itemToSearch < arrInput[middleElementIndex]:

                leftArray = arrInput[0:middleElementIndex]
                return binarySearch(leftArray, itemToSearch)

            else:

                rightArray = arrInput[middleElementIndex:len(arrInput)]
                return binarySearch(rightArray, itemToSearch)

        else:
            return -1


def insertionSort(arrInput):

    # This loop would run from [4, 2, 9, 3, 5]
    for i in range(1, len(arrInput)):

        # print(arrInput[i])
        key = arrInput[i]
        j = i - 1  # It would start with 0th position

        # In actual insertion sort we perform below operation
        ## Move elements of arrInput[0...i-1], that are greater than key, to one position ahead of
        ## their current position.

        # But to reduce down the complexity we can use binary search to find correct location.
        loc = binarySearch(arrInput, key);

        while (j >= loc):
            arrInput[j + 1] = arrInput[j]
            j = j - 1

        arrInput[j + 1] = key

    return arrInput

if __name__ == '__main__':

    arrInput = [1, 4, 2, 9, 3, 5]
    sortedArr = insertionSort(arrInput)

    print(sortedArr)