def getDNASubsequenceList(dna,lengthToLookFor):

    subsequenceList = []
    isAlreadyPresent = {}

    startIndex = 0
    endIndex = lengthToLookFor

    while(endIndex<=len(dna)):

        subsequenceStr = dna[startIndex:endIndex]

        print(subsequenceStr)

        if subsequenceStr in isAlreadyPresent:
            subsequenceList.append(subsequenceStr)
            #isAlreadyPresent[subsequenceStr] = isAlreadyPresent[subsequenceStr] + 1
        else:
            isAlreadyPresent[subsequenceStr] = 1

        startIndex = startIndex + 1
        endIndex = endIndex + 1

    print(isAlreadyPresent)
    return subsequenceList

if __name__ == '__main__':

    dna = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    lengthToLookFor = 10
    subsequenceList = getDNASubsequenceList(dna,lengthToLookFor)

    print(subsequenceList)


