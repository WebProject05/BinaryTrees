class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfString = False


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insertString(self, word):
    current = self.root

    for i in word:
      ch = i
      node = current.children.get(ch) # This is to check whether the node already exists in the tree or not
      if (node == None):
        node = TrieNode()
        current.children.update({ch:node})
      current = node
    current.endOfString = True
    print("Inserted!")



  def searchString(self, word):
    currentNode = self.root
    for i in word:
      node = currentNode.children.get(i)
      if (node == None):
        return False
      
      currentNode = node
    if (currentNode.endOfString == True):
      return True
    else:
      return False



newTrie = Trie()  #Initialiaztion of the trie class
newTrie.insertString("San")
newTrie.insertString("Sant")
newTrie.insertString("Santo")
newTrie.insertString("Santos")
newTrie.insertString("Santosh")


print(newTrie.searchString("San"))
print(newTrie.searchString("Sanosh"))