def __swap(arrInput,i,k):

    temp = arrInput[i]
    arrInput[i] = arrInput[k]
    arrInput[k] = temp

def __bubbleSort(decimalBinaryList):

    for i in range(0,len(decimalBinaryList)):
        for j in range(i+1,len(decimalBinaryList)):
            decimal_i,binary_count_i = decimalBinaryList[i]
            decimal_j, binary_count_j = decimalBinaryList[j]

            if binary_count_i > binary_count_j :
                __swap(decimalBinaryList,i,j)
            elif (binary_count_i == binary_count_j) and decimal_i > decimal_j:
                __swap(decimalBinaryList,i,j)

def __decimalToBinary(decimalValue):

    return bin(decimalValue).replace('0b','')

def __countOfOnes(eachBinaryStr):

    count = 0

    for eachChar in eachBinaryStr:
        if eachChar == "1":
            count = count + 1

    return count

def getSortedArray(inputArr):

    decimalBinaryList = []

    for eachDecimal in inputArr:
        decimalBinaryList.append((eachDecimal,__countOfOnes(__decimalToBinary(eachDecimal))))

    print(decimalBinaryList)
    __bubbleSort(decimalBinaryList)
    return decimalBinaryList

if __name__ == '__main__':

    inputArr = [5,6,3,10,7,14]

    sortedArrList = getSortedArray(inputArr)
    print(sortedArrList)
