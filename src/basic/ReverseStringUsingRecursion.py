'''
    Below script shows a sample of how we can reverse one string.
    This is an inplace reverse algorithm.
    This script also shows some of the standard method to reverse one string using it chars.
'''

def getPythonicReversedStr(inputStr):

    '''
        Function to reverse the string using python built in functions.
    :param inputStr:
    :return: Reversed string.
    '''

    if inputStr and len(inputStr) > 0:
        return "".join(reversed(inputStr))

def getNaturalReversedStr(inputStr):
    '''
        Function to reverse string using for/while loop.
    :param inputStr: Actual string value
    :return: reversed string

    '''

    reversedStr = ""

    length = len(inputStr)
    if inputStr and length > 0:

        while(length>0):

            reversedStr = reversedStr + inputStr[length-1]
            length = length - 1

        return reversedStr

def getReversedStr(inputStr):

    '''

       Function to reverse the string using recursion.
    :param inputStr:
    :return: Return reversed string.

    '''

    if len(inputStr) == 1:
        return inputStr
    else:
        return inputStr[len(inputStr)-1] + getReversedStr(inputStr[0:len(inputStr)-1])

if __name__ == '__main__':

    inputStr = "sumit"
    reversedStr = getReversedStr(inputStr)
    print(reversedStr)

    reversedStr2 = getNaturalReversedStr(inputStr)
    print(reversedStr2)

    reversedStr3 = getPythonicReversedStr(inputStr)
    print(reversedStr3)


