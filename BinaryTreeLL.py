class TreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None



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


# Search in Binary Tree (Level Order Traversal)
def searchBT(rootNode, node):
  if not rootNode:
    return "The tree is empty"
  
  queue = [rootNode]
  while queue:
    current = queue.pop(0)   # dequeue
    if current.data == node:
      return f"Node '{node}' found in the tree."
    
    if current.leftChild:
      queue.append(current.leftChild)
    if current.rightChild:
      queue.append(current.rightChild)
  
  return f"Node '{node}' not found in the tree."


def insertNodeBT(rootNode, newNode):
  if not rootNode:
    rootNode = newNode
    return
  
  queue = [rootNode]
  while queue:
    current = queue.pop(0)

    if (current.leftChild is None):
      current.leftChild = newNode
      return
    else:
      queue.append(current.leftChild)

    if (current.rightChild is None):
      current.rightChild = newNode
      return
    else:
      queue.append(current.rightChild)


# Delete node from binary tree

def getDeepestNode(rootNode):
  if not rootNode:
    return None
  
  queue = [rootNode]  
  while queue:
    current = queue.pop(0)
    if current.leftChild:
      queue.append(current.leftChild)
    if current.rightChild:
      queue.append(current.rightChild)

    return current

def deleteDeepestNode(rootNode, dNode):
  queue = [rootNode]
  while queue:
    current = queue.pop(0)
    if current is dNode:
      current = None
      return
    if current.leftChild:
      if current.leftChild is dNode:
        current.leftChild = None
        return
      else:
        queue.append(current.leftChild)
    if current.rightChild:
      if current.rightChild is dNode:
        current.rightChild = None
        return
      else:
        queue.append(current.rightChild)


# Delete a given node by value
def deleteNodeBT(rootNode, nodeValue):
  if not rootNode:
    return "The tree is empty"

  queue = [rootNode]
  while queue:
    current = queue.pop(0)
    if current.data == nodeValue:
      deepestNode = getDeepestNode(rootNode)
      current.data = deepestNode.data   # replace data
      deleteDeepestNode(rootNode, deepestNode)
      return f"Node '{nodeValue}' deleted"
    if current.leftChild:
      queue.append(current.leftChild)
    if current.rightChild:
      queue.append(current.rightChild)

  return f"Node '{nodeValue}' not found"



def deleteBT(rootNode):
  rootNode.data = None
  rootNode.leftChild = None
  rootNode.rightChild = None
  return "The Binary Tree has been deleted!"




# Create Tree
newBt = TreeNode("Home")
leftChild = TreeNode("College")
rightChild = TreeNode("Park")
leftChild_left = TreeNode("Class Rooms")

newBt.leftChild = leftChild
newBt.rightChild = rightChild
leftChild.leftChild = leftChild_left


newNode = TreeNode("Bed")



# Driver Code
print("----PreOrder----")
preOrderTraversal(newBt)

print("----InOrder-----")
inOrderTraversal(newBt)

print("----PostOrder----")
postOrderTraversal(newBt)

print("----LevelOrder----")
levelOrderTraversal(newBt)


print("---Insert node in binary tree---")
insertNodeBT(newBt, newNode)
levelOrderTraversal(newBt)