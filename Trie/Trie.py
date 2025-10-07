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

def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    # Case 1: Word doesn't exist
    if currentNode is None:
        return False

    # Case 2: Still traversing through nodes
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False

    # Case 3: Reached last character of the word
    if index == len(word) - 1:
        # Word not found as valid string
        if currentNode.endOfString == False:
            return False
        # Unmark endOfString
        currentNode.endOfString = False
        # If no children, we can delete this node
        if len(currentNode.children) == 0:
            root.children.pop(ch)
            return True
        else:
            return False

    # Case 4: Recursive call for next character
    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)

    # Delete child node reference if it can be deleted
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        # Check if current node is deletable now
        return not root.endOfString and len(root.children) == 0
    return False


newTrie = Trie()  #Initialiaztion of the trie class
newTrie.insertString("San")
newTrie.insertString("Sant")
newTrie.insertString("Santo")
newTrie.insertString("Santos")
newTrie.insertString("Santosh")


print(newTrie.searchString("San"))
print(newTrie.searchString("Sanosh"))