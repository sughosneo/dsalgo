'''

    This script helps to understand few of the standard Hash function provided by Python3
    - Few of the samples have been defined in here.
    - This class file could also be be useful as helper class to any other module.
    - hashlib is the standard library , which has been referenced in here. Reference as per below :

    https://docs.python.org/3/library/hashlib.html
    https://www.pythoncentral.io/hashing-strings-with-python/
'''

import hashlib

class Hashing:

    def __init__(self):
        pass

    '''
        Widely use hashing producing 128-bit hash value. 
        Used to check data integrity.
    '''
    def getMD5Hash(self,inputStr):

        if inputStr :

            encodedStr = inputStr.encode('utf-8')
            hash_object = hashlib.md5(encodedStr)
            hex_dig = hash_object.hexdigest()

            return hex_dig

        else :
            raise Exception("Input string value is None")


    '''
        More secure Hashing - message length comes between 160 bits to 512 bits, based on which following function gets called.
        SHA1,SHA224,SHA256,SHA384,SHA512
    '''
    def getSHA256(self,inputStr):

        if inputStr :

            encodedStr = inputStr.encode('utf-8')
            hash_object = hashlib.sha256(encodedStr)
            hex_dig = hash_object.hexdigest()

            return hex_dig

        else :
            raise Exception("Input string value is None")

if __name__ == '__main__':

    inputStr = "CAT"

    hashing = Hashing()

    hashedMD5Value = hashing.getMD5Hash(inputStr)
    n = int(hashedMD5Value, base=16)
    print(n)

    hashedSHAValue = hashing.getSHA256(inputStr)
    n = int(hashedSHAValue, base=16)
    print(n)