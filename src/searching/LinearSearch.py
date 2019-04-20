def linearSearch(arrInput,itemToSearch):

    isPresent = False

    for k in range(0,len(arrInput)):

        if itemToSearch == arrInput[k]:
            isPresent = True

    return isPresent

if __name__ == '__main__':

    arrInput = [1, 4, 2, 9, 3, 5]

    # Present
    isPresent = linearSearch(arrInput,9)
    print(isPresent)

    # Not Present
    isPresent = linearSearch(arrInput, 10)
    print(isPresent)
