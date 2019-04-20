def swap(arrInput,i,k):

    temp = arrInput[i]
    arrInput[i] = arrInput[k]
    arrInput[k] = temp

def bubbleSort(arrInput):

    for i in range(0,len(arrInput)):
        for k in range(i+1,len(arrInput)):

            if arrInput[i] > arrInput[k]:
                swap(arrInput,i,k)

    return arrInput


if __name__ == '__main__':

    arrInput = [1, 4, 2, 9, 3, 5]
    sortedArr = bubbleSort(arrInput)

    print(sortedArr)