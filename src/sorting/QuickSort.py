# Still there is some problem which needs to be sorted out.
# Ref : https://www.youtube.com/watch?v=SLauY6PpjW4

def quickSortWrapper(arr):

    quickSort(arr,0,len(arr)-1)

def partition(arr,low,high,pivot):

    print(arr)

    while (low <= high) :

        while(arr[low] < pivot) :
            low += 1

        while(arr[high] > pivot):
            high -= 1

        if low <= high:
            arr[low],arr[high] = arr[high],arr[low]
            low += 1
            high -= 1

        # This is the further partition index.
        return low

def quickSort(arr,start,end):

    # If left overlaps with right then stop it.
    if start < end :

        middle = (start + end) // 2
        pivot = arr[middle]
        print(pivot)

        pi = partition(arr,start,end,pivot)

        quickSort(arr,start,pi-1)
        quickSort(arr,pi,end)


if __name__ == '__main__':
    arr = [1,4,2,9,3,5]
    #arr = [9,2,6,4,3,5,1]

    quickSortWrapper(arr)
    print(arr)