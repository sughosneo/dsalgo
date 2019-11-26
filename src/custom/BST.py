'''
    This is another BST implementation with Level Order Traversal.
    It could be a very good example of demoing the functionality of how object reference does work in Python
'''

from collections import deque

class Node:

    left = None
    right = None
    value = None

    def __init__(self,nodeValue):
        self.left = None
        self.right = None
        self.value = nodeValue


class BST:

    __root = None
    __totalNumberOfElements = None

    def __init__(self):
        self.__root = None
        self.__totalNumberOfElements = 0

    def insert(self,node):

        if node and node.value:

            if self.__root == None:

                self.__root = node
                self.__totalNumberOfElements +=1
            else:

                current = self.__root
                previous = None

                # Run this loop until current value is not null.
                while(current):

                    previous = current

                    if node.value < current.value:
                        current = current.left
                    else:
                        current = current.right


                if node.value < previous.value :
                    previous.left = node
                else:
                    previous.right = node

                self.__totalNumberOfElements += 1

    def inOrderTraversal(self,root):

        if root :
            self.inOrderTraversal(root.left)
            print(root.value)
            self.inOrderTraversal(root.right)

    def levelOrderTraversal(self,root):

        q = deque()

        q.append(root)

        while(len(q) > 0):

            popedNode = q.popleft()
            print(popedNode.value)

            if popedNode.left :
                q.append(popedNode.left)

            if popedNode.right :
                q.append(popedNode.right)

    def getNoOfElements(self):

        return self.__totalNumberOfElements

    def getRootElement(self):

        return self.__root


if __name__ == '__main__':

    bst = BST()

    bst.insert(Node(100))
    # print(bst.getNoOfElements())
    # print(bst.getRootElement().value)

    bst.insert(Node(20))
    bst.insert(Node(500))
    bst.insert(Node(10))
    bst.insert(Node(30))
    bst.insert(Node(40))

    print("Root=>",bst.getRootElement().value)
    print("-----------")

    bst.inOrderTraversal(bst.getRootElement())

    print("-----------")

    bst.levelOrderTraversal(bst.getRootElement())