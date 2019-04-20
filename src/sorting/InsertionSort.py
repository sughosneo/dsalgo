def insertionSort(arrInput):

    # arrInput - [1, 4, 2, 9, 3, 5]
    #             0  1  2  3  4  5

    # This loop would run from [4, 2, 9, 3, 5]
    for i in range(1,len(arrInput)):

        #print(arrInput[i])
        key = arrInput[i]
        j = i - 1 # It would start with 0th position

        ## Move elements of arrInput[0...i-1], that are greater than key, to one position ahead of
            ## their current position.

        while(j>=0 and arrInput[j]> key):

            arrInput[j+1] = arrInput[j]
            j = j -1

        arrInput[j + 1] = key

    return arrInput

if __name__ == '__main__':

    arrInput = [1, 4, 2, 9, 3, 5]
    sortedArr = insertionSort(arrInput)

    print(sortedArr)



