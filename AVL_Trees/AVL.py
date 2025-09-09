# The avl tree is a balanced version of BST, where if the height difference 
# of the heights is more than one then rotation is needed and if not it is not needed. 
# In case of inserting a node we have to follow this rotation.

"""
if the left sub tree height is 5 and right sub tree is 4
then the height difference is 1 so it is satisfying avl tree condition. 
If it is like 5 and 3 the difference is more than one (>1) 
then the avl tree condition is not satisfied so we need rotations.
"""

class AVLNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None    
    self.rightChild = None
    self.height = 1


# PreOrder Traversal
def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)


# InOrder Traversal
def inOrderTraversal(rootNode):
  if not rootNode:
    return
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)


# PostOrder Traversal
def postOrderTraversal(rootNode):
  if not rootNode:
    return
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild)
  print(rootNode.data)


# Level Order Traversal (using list as queue)
def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  queue = [rootNode]
  while queue:
    current = queue.pop(0)   # dequeue
    print(current.data)
    if current.leftChild:
      queue.append(current.leftChild)
    if current.rightChild:
      queue.append(current.rightChild)


def searchNode(rootNode, value):
  if not rootNode:
    print("Value not found")
    return
  if rootNode.data == value:
    print("The value is found")
  elif value < rootNode.data:
    searchNode(rootNode.leftChild, value)
  else:
    searchNode(rootNode.rightChild, value)


def getHeight(rootNode):
  if not rootNode:
    return 0
  return rootNode.height


def rightRotate(disbalancedNode):
  newRoot = disbalancedNode.leftChild
  disbalancedNode.leftChild = newRoot.rightChild
  newRoot.rightChild = disbalancedNode
  disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), 
                                   getHeight(disbalancedNode.rightChild))
  newRoot.height = 1 + max(getHeight(newRoot.leftChild), 
                           getHeight(newRoot.rightChild))
  return newRoot


def leftRotate(disbalancedNode):
  newRoot = disbalancedNode.rightChild
  disbalancedNode.rightChild = newRoot.leftChild
  newRoot.leftChild = disbalancedNode
  disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), 
                                   getHeight(disbalancedNode.rightChild))
  newRoot.height = 1 + max(getHeight(newRoot.leftChild), 
                           getHeight(newRoot.rightChild))
  return newRoot


def getBalanced(rootNode):
  if not rootNode:
    return 0
  return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
  if not rootNode:
    return AVLNode(nodeValue)
  elif nodeValue < rootNode.data:
    rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
  else:
    rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

  rootNode.height = 1 + max(getHeight(rootNode.leftChild), 
                            getHeight(rootNode.rightChild))
  balance = getBalanced(rootNode)

  # Case 1 - Left Left
  if balance > 1 and nodeValue < rootNode.leftChild.data:
    return rightRotate(rootNode)
  # Case 2 - Left Right
  if balance > 1 and nodeValue > rootNode.leftChild.data:
    rootNode.leftChild = leftRotate(rootNode.leftChild)
    return rightRotate(rootNode)
  # Case 3 - Right Right
  if balance < -1 and nodeValue > rootNode.rightChild.data:
    return leftRotate(rootNode)
  # Case 4 - Right Left
  if balance < -1 and nodeValue < rootNode.rightChild.data:
    rootNode.rightChild = rightRotate(rootNode.rightChild)
    return leftRotate(rootNode)

  return rootNode


newAVL = AVLNode(10)
newAVL = insertNode(newAVL, 3)
newAVL = insertNode(newAVL, 9)
newAVL = insertNode(newAVL, 4)
newAVL = insertNode(newAVL, 40)
newAVL = insertNode(newAVL, 30)

# This is Level Order Traversal for the AVL trees
print("Level Order Traversal of AVL Tree: ")
levelOrderTraversal(newAVL)
