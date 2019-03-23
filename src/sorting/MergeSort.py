# Merge sort seems to be fine with all corner scenario :
# Ref : https://www.geeksforgeeks.org/merge-sort/

def mergeSortWrapper(arr):

    return mergeSort(arr)

def mergeBothHalves(arr,leftArr,rightArr):

    print(leftArr)
    print(rightArr)
    print("-----")

    leftArrIndex = 0
    rightArrIndex = 0
    index = 0

    while(leftArrIndex < len(leftArr) and rightArrIndex < len(rightArr)):

        if (leftArr[leftArrIndex] < rightArr[rightArrIndex]):
            arr[index] = leftArr[leftArrIndex]
            leftArrIndex += 1
            index += 1
        else:
            arr[index] = rightArr[rightArrIndex]
            rightArrIndex += 1
            index += 1

    while(leftArrIndex < len(leftArr)) :
        arr[index] = leftArr[leftArrIndex]
        leftArrIndex += 1
        index += 1

    while(rightArrIndex < len(rightArr)) :
        arr[index] = rightArr[rightArrIndex]
        rightArrIndex += 1
        index += 1

    print(arr)
    print("====")
    return arr


def mergeSort(arr):

    if len(arr) > 1:

        middle = len(arr) // 2
        leftArr = arr[:middle]
        rightArr = arr[middle:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        return mergeBothHalves(arr,leftArr,rightArr)


if __name__ == '__main__':

    # print("Please provide input array below and press enter after that ::")
    # rawInput = input()
    # arrInput = [int(x) for x in input().split(" ")]
    # print("Input Array",arrInput)
    arrInput = [1,4,2,9,3,5]
    sortedArr = mergeSortWrapper(arrInput)

    print(sortedArr)
