class Graphs:
  def __init__(self, graphDict = None):
    if graphDict is None:
      graphDict = {}
    self.graphDict = graphDict


  # def addEdge(self, vertex, edge):
  #   self.graphDict[vertex].append(edge)


  def addVertex(self, vertex):
    if vertex not in self.graphDict.keys():
      self.graphDict[vertex] = []
      return True
    return False
  
  def printGraph(self):
    for vertex in self.graphDict.keys():
      print(vertex , ":", self.graphDict[vertex])


  def addEdge(self, vertex1, vertex2):
    # Auto-create vertices if missing
    if vertex1 not in self.graphDict:
      self.graphDict[vertex1] = []
    if vertex2 not in self.graphDict:
      self.graphDict[vertex2] = []

    # Avoid duplicate edges
    if vertex2 not in self.graphDict[vertex1]:
      self.graphDict[vertex1].append(vertex2)
    if vertex1 not in self.graphDict[vertex2]:
      self.graphDict[vertex2].append(vertex1)

    return True
  
  def removeEdge(self, vertex1, vertex2):
    if vertex1 in self.graphDict and vertex2 in self.graphDict[vertex1]:
      self.graphDict[vertex1].remove(vertex2)
    if vertex2 in self.graphDict and vertex1 in self.graphDict[vertex2]:
      self.graphDict[vertex2].remove(vertex1)


  def removeVertex(self, vertex):
    if vertex in self.graphDict:
      for otherVertex in self.graphDict[vertex]:
        self.graphDict[otherVertex].remove(vertex)
      del self.graphDict[vertex]
      return True
    return False



# customGraph = {
#   "a": ["b", "c"],   #meaning that a has two edges which connect ot b and c
#   "b": ["a", "d", "e"],
#   "c": ["a", "e"],
#   "d": ["b", "e", "f"],
#   "e": ["d", "f", "c"],
#   "f": ["d", "e"]
# }

customGraph = {}

graph = Graphs(customGraph)
graph.addVertex("a")
graph.addVertex("b")
graph.addVertex("c")
graph.addEdge("a", "b")
graph.addEdge("a", "c")
graph.removeEdge("a", "c")
graph.removeVertex("c")

graph.printGraph()