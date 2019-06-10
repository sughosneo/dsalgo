'''
    Below script actually helps to partition one array based on a window.
'''
def partition(arrayList,partitionWindow):

    left = 0
    right = len(arrayList) - 1

    traverse = 0

    while(traverse<=right):

        if arrayList[traverse] < partitionWindow:

            arrayList[left],arrayList[traverse] = arrayList[traverse],arrayList[left]
            left=left +1
            traverse = traverse + 1
        elif arrayList[traverse] > partitionWindow:
            arrayList[right], arrayList[traverse] = arrayList[traverse], arrayList[right]
            right = right - 1
            traverse = traverse + 1
        else:
            traverse = traverse + 1

    return arrayList



if __name__ == '__main__':

    partitionWindow = 5
    #arrayList = [3,4,5,6,5]
    arrayList = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]

    modifiedArray = partition(arrayList,partitionWindow)

    print(modifiedArray)