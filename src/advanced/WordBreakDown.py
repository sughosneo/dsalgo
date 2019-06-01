def IsValidWordPresent(wordList,inputStr):

    sequenceChar = ""
    availableWordList = []

    for eachChar in inputStr:

        sequenceChar = sequenceChar + eachChar

        print(sequenceChar)

        if sequenceChar in wordList:

            availableWordList.append(sequenceChar)
            # Rest the sequence char as ""
            sequenceChar = ""

    #print(availableWordList)

    if availableWordList  and len(availableWordList) > 0 :

        formedStr = "".format(availableWordList)

        if inputStr == formedStr:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':

    wordList = ["arrays", "dynamic", "heaps", "IDeserve", "learn", "learning", "linked", "list", "platform", "programming", "stacks", "trees"]

    inputStr = "IDeservelearningplatform"

    isPresent = IsValidWordPresent(wordList,inputStr)

    print(isPresent)