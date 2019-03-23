'''

    This is the Binary Search Tree Implementation using linked list.

    Proper Binary Search Tree Looks like as per below :

      9
    /  \
   5    14
  / \   / \
 3   6  12 16

- In Order Traversal
- Pre-Order Traversal
- Invertion / Mirror of the tree
- Again pre-order traversal

'''

class Node :

    value = None
    leftChild = None # Each left child of type Node class
    rightChild = None # Each left child of type Node class

    def __init__(self,nodeValue):
        self.value = nodeValue
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree :

    # This root is basically type of Node class.
    __root = None
    __totalNumberOfElements = 0

    def __init__(self):
        self.__root = None

    def getRootNode(self):
        return self.__root

    def insertAItem(self, newNode):

        # First check if the newNode has some data or not, then proceed with adding

        if newNode and newNode.value :

            # That means root element is empty.
            # This would be the first addition to the node.
            if self.__root == None:
                self.__root = newNode
                self.__totalNumberOfElements = self.__totalNumberOfElements + 1

            else:

                currentNode = self.__root
                parentNode = None

                # Loop through always each element in the tree.
                while(True):

                    # Check with the root node to see if value is less than current value.
                    parentNode = currentNode

                    if newNode.value < currentNode.value:
                        # Proceed with left child
                        currentNode = currentNode.leftChild

                        if currentNode == None:
                            parentNode.leftChild = newNode
                            self.__totalNumberOfElements = self.__totalNumberOfElements + 1

                            return 1
                    else:
                        # Proceed with right child.
                        currentNode = currentNode.rightChild

                        if currentNode == None:
                            parentNode.rightChild = newNode
                            self.__totalNumberOfElements = self.__totalNumberOfElements + 1

                            return 1
        else:
            return -1

    def sizeOfTree(self):

        return self.__totalNumberOfElements


    def inOrderTraversal(self,root):

        # If root node is not empty
        if root:

            self.inOrderTraversal(root.leftChild)
            print(root.value)
            self.inOrderTraversal(root.rightChild)


    def preOrderTraversal(self,root):

        if root:
            print(root.value)
            self.preOrderTraversal(root.leftChild)
            self.preOrderTraversal(root.rightChild)


    def invertedTree(self,root):

        if root:

            # Swap the left and right child of each node.

            temp = root.leftChild
            root.leftChild = root.rightChild
            root.rightChild = temp

            # Invert all the left child.
            self.invertedTree(root.leftChild)

            # Invert all the right child.
            self.invertedTree(root.rightChild)



if __name__ == '__main__':

    # Initializa the Binary Search Tree
    bst = BinarySearchTree()

    #region // insertion to tree
    node = Node(9)        # Create a node
    bst.insertAItem(node) # Add it to the tree
    print("Root node now:",bst.getRootNode())
    print("Size of the tree:", bst.sizeOfTree())

    node = Node(5)
    bst.insertAItem(node)
    print("Root node now:", bst.getRootNode())
    print("Size of the tree:", bst.sizeOfTree())


    node = Node(14)
    bst.insertAItem(node)
    print("Root node now:", bst.getRootNode())
    print("Size of the tree:", bst.sizeOfTree())

    node = Node(3)
    bst.insertAItem(node)
    print("Root node now:", bst.getRootNode())
    print("Size of the tree:", bst.sizeOfTree())

    node = Node(6)
    bst.insertAItem(node)
    print("Root node now:", bst.getRootNode())
    print("Size of the tree:", bst.sizeOfTree())

    node = Node(12)
    bst.insertAItem(node)
    print("Root node now:", bst.getRootNode())

    node = Node(16)
    bst.insertAItem(node)
    print("Root node now:", bst.getRootNode())

    #endregion // instertion to the tree ends in here.

    #region // inorder Traversal binarysearchtree
    print("In Order Traversal Of the Tree")
    rootNode = bst.getRootNode()
    print("root node value:",rootNode.value)
    bst.inOrderTraversal(rootNode)
    #endregion

    #region // preorder Traversal binarysearchtree
    print("Pre Order Traversal Of the Tree")
    rootNode = bst.getRootNode()
    print("root node value:", rootNode.value)
    bst.preOrderTraversal(rootNode)
    #endregion


    #region // Invertion or mirror of the Binary Search Tree
    rootNode = bst.getRootNode()
    bst.invertedTree(rootNode)
    print("Pre Order traversal of the inverted Binary Search Tree")
    rootNode = bst.getRootNode()
    bst.preOrderTraversal(rootNode)
    #endregion
