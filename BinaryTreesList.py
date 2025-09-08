# The childs of a node which is at an index of i are at 2i nd 2i + 1
# The indexing starts from 1 not zero

class BinaryTree():
  def __init__(self, size):
    self.customList = size * [None]
    self.lastUsedIndex = 0
    self.maxSize = size

  def insertNode(self, value):
    if self.lastUsedIndex + 1 == self.maxSize:
      return "The Binary tree is full"
    
    self.customList[self.lastUsedIndex + 1] = value
    self.lastUsedIndex += 1
    return "The value has been successfully inserted"
  

  def searchNode(self, Value):
    for i in range(len(self.customList)):
      if (self.customList[i] == Value):
        return "Found"
    return "Not Found"

  def preOrderTraversal(self, index):
    if index > self.lastUsedIndex:
      return
    print(self.customList[index])
    self.preOrderTraversal(index * 2)   # Visiting the left sub tree
    self.preOrderTraversal(index * 2 + 1)   #Visiting the right sub tree


  def inOrderTraversal(self, index):
    if index > self.lastUsedIndex:
      return
    self.inOrderTraversal(index * 2)
    print(self.customList[index])
    self.inOrderTraversal(index * 2 + 1)

  def postOrderTraversal(self, index):
    if index > self.lastUsedIndex:
      return
    self.postOrderTraversal(index * 2)
    self.postOrderTraversal(index * 2 + 1)
    print(self.customList[index])

  def levelOrderTraversal(self, index):
    for i in range(index, self.lastUsedIndex+1):
      print(self.customList[i])

    
  def deleteNode(self, value):
    if self.lastUsedIndex == 0:
      return "There is no node to delete"
    for i in range(1, self.lastUsedIndex+1):
      if self.customList[i] == value:
        self.customList[i] = self.customList[self.lastUsedIndex]
        self.customList[self.lastUsedIndex] = None
        self.lastUsedIndex -= 1
        return "The Node has been succesfully deleted"
      
  def deleteBT(self):
    self.customList = None
    return "The binary tree is deleted"


newBT = BinaryTree(10)

newBT.insertNode(10)
newBT.insertNode(20)
newBT.insertNode(40)
newBT.insertNode(90)
newBT.insertNode(30)
# print(newBT.searchNode(220))

print("---PreOrder---")
newBT.preOrderTraversal(1)

print("---InOrder---")
newBT.inOrderTraversal(1)

print("---PostOrder---")
newBT.postOrderTraversal(1)