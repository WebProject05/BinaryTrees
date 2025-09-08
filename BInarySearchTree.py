# The basic conecpt of this tree is that what ever the value which is lesser than the root node will be placed in the left sub tree and the greater one in the right sub tree
from collections import deque


class BSTNode():
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None


def insertNode(rootNode, nodeValue):
  if (rootNode.data == None):
    rootNode.data = nodeValue
  elif nodeValue <= rootNode.data:
    if (rootNode.leftChild is None):
      rootNode.leftChild = BSTNode(nodeValue)
    else:
      insertNode(rootNode.leftChild, nodeValue)
  else:
    if (rootNode.rightChild is None):
      rootNode.rightChild = BSTNode(nodeValue)
    else:
      insertNode(rootNode.rightChild, nodeValue)

  return "The node is inserted"


def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)



def inOrderTraversal(rootNode):
  if not rootNode:
    return
  
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)



def postOrderTraversal(rootNode):
  if not rootNode:
    return
  
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild)
  print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    
    queue = deque()
    queue.append(rootNode)

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.leftChild:
            queue.append(current.leftChild)
        if current.rightChild:
            queue.append(current.rightChild)


def searchBST(rootNode, value):
  if not rootNode:
    return
  if rootNode.data == value:
    print(f"Node {value} is found")
  elif (value <= rootNode.data):
    if rootNode.leftChild.data == value:
      print(f"Node {value} is found")
    else:
      searchBST(rootNode.leftChild, value)
  else:
    if rootNode.rightChild.data == value:
      print(f"Node {value} is found")
    else:
      searchBST(rootNode.rightChild, value)




def minimumNode(rootNode):
    current = rootNode
    while current.leftChild is not None:
        current = current.leftChild
    return current


def deleteNode(rootNode, value):
    if rootNode is None:
        return rootNode

    # Traverse to find the node
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        # Case 1: Node has no left child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        # Case 2: Node has no right child
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        # Case 3: Node has two children
        temp = minimumNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    return rootNode


def deleteBST(rootNode):
   rootNode.data = None
   rootNode.leftChild = None
   rootNode.rightChild = None
   print("The binary search tree has been deleted!")




newBST = BSTNode(None)  # Assigning a root Node
insertNode(newBST, 190)
insertNode(newBST, 129)
insertNode(newBST, 124)
insertNode(newBST, 98)
insertNode(newBST, 87)
insertNode(newBST, 34)
insertNode(newBST, 50)
insertNode(newBST, 30)


levelOrderTraversal(newBST)
print("\n")
searchBST(newBST, 98)



deleteNode(newBST, 87)
levelOrderTraversal(newBST)