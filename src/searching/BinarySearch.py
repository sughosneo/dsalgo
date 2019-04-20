
# We would keep on splitting up the array until we match last element.
def binarySearch(arrInput,itemToSearch):
    '''

    :param arrInput: Input array where we would need to find the value.
    :param itemToSearch:
    :return bool:

    '''


    middleElementIndex = len(arrInput) // 2

    print(middleElementIndex)

    if itemToSearch == arrInput[middleElementIndex]:
        return True
    else:

        if len(arrInput) > 1:

            # Means if searchable item value is less than middle element.
            if itemToSearch < arrInput[middleElementIndex]:

                leftArray = arrInput[0:middleElementIndex]
                return binarySearch(leftArray,itemToSearch)

            else:

                rightArray = arrInput[middleElementIndex:len(arrInput)]
                return binarySearch(rightArray,itemToSearch)

        else:
            return False




if __name__ == '__main__':

    # Array needs to be a sorted array for Binary Search to work.
    arrInput = [1, 2, 3, 4, 5, 9]
    #arrInput = [2]

    # Present
    isPresent = binarySearch(arrInput, 5)
    print(isPresent)

    # Not Present
    isPresent = binarySearch(arrInput, 10)
    print(isPresent)
