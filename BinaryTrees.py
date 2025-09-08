# The Below Code is using Arrays (list)

class TreeNode:
  def __init__(self, data, children = []):
    self.data = data
    self.children = children

  def __str__(self, level = 0):
    ret = " " * level + str(self.data) + "\n"
    for child in self.children:
      ret += child.__str__(level + 1)
    return ret
  

  def addChild(self, TreeNode):
    self.children.append(TreeNode)


tree = TreeNode('Stsh', [])
tree1 = TreeNode('rja', [])
tree2 = TreeNode('prsna', [])

tree.addChild(tree1)
tree.addChild(tree2)


# new children for the existent children
tree11 = TreeNode('ma', [])
tree12 = TreeNode('tate', [])

tree21 = TreeNode('ama', [])
tree22 = TreeNode('tat', [])

tree1.addChild(tree11)
tree1.addChild(tree12)

tree2.addChild(tree21)
tree2.addChild(tree22)


print(tree)