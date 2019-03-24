'''

    This script helps to understand one small sample implementation of Bloom Filter, which is known as Probalistic Data Structures.
    Anyone can understand and read about Bloom Filter from these below references :

    - https://blog.medium.com/what-are-bloom-filters-1ec2a50c68ff
    - https://www.youtube.com/watch?v=Bay3X9PAX5k
'''

from dsalgo.src.basic.Hashing import Hashing

class BloomFilter:

    hashTrackerBitArray = []
    hashHelper = None

    def __init__(self):

        # Assign this list with all zeros.
        # It would act has as bit array with all 0 values.
        for i in range(300):
            self.hashTrackerBitArray.append(0)


        self.hashHelper = Hashing()

    def isPresent(self,simpleHashedIntValue, oneByteIntValue):

        if simpleHashedIntValue and oneByteIntValue :

            fetchedFirstFlagValue = self.hashTrackerBitArray[simpleHashedIntValue]
            fetchedSecondFlagValue = self.hashTrackerBitArray[oneByteIntValue]

            # print("fetchedFirstFlagValue",fetchedFirstFlagValue)
            # print("fetchedSecondFlagValue", fetchedSecondFlagValue)

            if fetchedFirstFlagValue == 1 and fetchedSecondFlagValue == 1 :
                return "YES"
            else:
                return "NO"

    '''
        For provided string we calculate 2 set of hashed int value.
        To keep the implementation simple we are keeping only 2 simple hash calculation.
    '''
    def getTwoCorrespondingHashedValue(self,inputStr):

        try:

            simpleHashedIntValue = self.hashHelper.getSimpleHasedValue(inputStr)
            oneByteIntValue = self.hashHelper.getOneByteHasedValue(inputStr)

            return simpleHashedIntValue, oneByteIntValue

        except Exception as error:
            print(error)

    '''
        This method would help to convert the binary representation to integer.
    '''
    def getConvertedIntValue(self):

        decimal = 0
        for digit in self.hashTrackerBitArray:
            decimal = decimal * 2 + int(digit)

        return decimal


if __name__ == '__main__':

    bloomFilter = BloomFilter()

    # region // Convert bit array representation to decimal
    decimalValue = bloomFilter.getConvertedIntValue()
    print("Initial binary list, which would be Zero!")
    print(decimalValue)
    # endregion

    #region // Make the prepopulated list.
    inputStr = "CAT"
    simpleHashedIntValue, oneByteIntValue = bloomFilter.getTwoCorrespondingHashedValue(inputStr)
    print(simpleHashedIntValue, oneByteIntValue)
    bloomFilter.hashTrackerBitArray[simpleHashedIntValue]  = 1
    bloomFilter.hashTrackerBitArray[oneByteIntValue] = 1

    inputStr = "DOG"
    simpleHashedIntValue, oneByteIntValue = bloomFilter.getTwoCorrespondingHashedValue(inputStr)
    print(simpleHashedIntValue, oneByteIntValue)
    bloomFilter.hashTrackerBitArray[simpleHashedIntValue] = 1
    bloomFilter.hashTrackerBitArray[oneByteIntValue] = 1

    inputStr = "HAT"
    simpleHashedIntValue, oneByteIntValue = bloomFilter.getTwoCorrespondingHashedValue(inputStr)
    print(simpleHashedIntValue, oneByteIntValue)
    bloomFilter.hashTrackerBitArray[simpleHashedIntValue] = 1
    bloomFilter.hashTrackerBitArray[oneByteIntValue] = 1

    #endregion

    print("Below is the bit array  after populating the item in the bit array list")
    print(bloomFilter.hashTrackerBitArray)

    #region // Check if BAT is present or not ?
    inputStr = "BAT"
    simpleHashedIntValue, oneByteIntValue = bloomFilter.getTwoCorrespondingHashedValue(inputStr)
    print(simpleHashedIntValue, oneByteIntValue)
    print("Is {} present already in the prepopulated list ?".format(inputStr))
    print(bloomFilter.isPresent(simpleHashedIntValue, oneByteIntValue))
    #endregion

    # region // Check if BAT is present or not ?
    inputStr = "CAT"
    simpleHashedIntValue, oneByteIntValue = bloomFilter.getTwoCorrespondingHashedValue(inputStr)
    print(simpleHashedIntValue, oneByteIntValue)
    print("Is {} present already in the prepopulated list ?".format(inputStr))
    print(bloomFilter.isPresent(simpleHashedIntValue, oneByteIntValue))
    # endregion

    #region // Convert bit array representation to decimal
    decimalValue = bloomFilter.getConvertedIntValue()
    print("Here is the decimal value for the updated binary list")
    print(decimalValue)
    #endregion