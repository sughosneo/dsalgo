'''
    Below program shows how permutation works for an input str.
'''

def getPermutatedStr(inputStr):

    allPermutationList = []

    allPermutationList.append(permutation("",inputStr))

    return allPermutationList

def permutation(perm,word):

    if word == "": # We don't have any letter left to be permutated.
        return perm + word
    else:
        # To start with the range value starts from 0 to 4
        for i in range(0,len(word)):
            permutation(perm+word[i],word[0:i]+word[(i+1),len(word)])


if __name__ == '__main__':

    inputStr = "sumit"

    allPermutatedStrList = getPermutatedStr(inputStr)
    print(allPermutatedStrList)

