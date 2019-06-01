'''
    This is Trie Datastructure. It's yet to get completed.
'''
class TrieNode:

    char = None
    children = None
    isEndOfWord = None

    def __init__(self,char):

        self.char = char
        self.children = []

        # isEndOfWord is True if this node represent the end of the word
        self.isEndOfWord = False

class Trie:

    __root = None
    __no_of_levels = None

    def __init__(self,root):
        self.__root = root
        self.__no_of_levels = 0

    def getTrieRoot(self):

        return self.__root

    def getNoOfLevels(self):

        return self.__no_of_levels

    def printAllValues(self):

        currentNode = self.__root

        noOfLevels = self.__no_of_levels

        for eachLevel in noOfLevels:

            print(currentNode.char)

    def insert(self,word:str) -> None:

        '''
            Insert one new word in trie data structure
        :param word:
        :return: None
        '''

        currentNode = self.__root

        # Set level :
        lengthOfWord = len(word)

        if lengthOfWord > self.__no_of_levels:
            self.__no_of_levels = lengthOfWord

        for char in word:

            found_in_child_list = False

            # Search for the character in the children of the present `node`
            for child in currentNode.children:

                if child.char == char:

                    # Reference point to that specific child.
                    currentNode = child
                    found_in_child_list = True

                    break

            # We did not find it so add a new chlid
            if not found_in_child_list:
                new_node = TrieNode(char)
                currentNode.children.append(new_node)

                # And then point node to the new child
                currentNode = new_node

        # Everything finished. Mark it as the end of a word.
        currentNode.word_finished = True


    def search(self,word):

        found_in_child_list = True

        # Search word in the trie
        # Returns true if key presents
        # in trie, else false

        currentNode = self.__root

        for char in word:

            # Search for the character in the children of the present `node`
            for child in currentNode.children:

                if child.char == char:
                    # Reference point to that specific child.
                    currentNode = child
                else:
                    found_in_child_list = False
                    break

            if not found_in_child_list:
                break

        return found_in_child_list


if __name__ == "__main__":

    root = TrieNode("*")

    trie = Trie(root)

    rootNode = trie.getTrieRoot()
    print(rootNode.char)

    trie.insert("the")
    trie.insert("there")
    trie.insert("their")
    #trie.insert("thereafter")

    print(trie.getNoOfLevels())

    #
    # print(trie.search("ther"))
    # print(trie.search("thei"))

