from collections import deque

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
  

  def BFS(self, vertex):      #Time complexity: O(V + E)   v -> number of vertex, e -> number of edges
    visited = set()           
    visited.add(vertex)       #Space complexity: O(V)
    queue = deque([vertex])
    while queue:
      current_vertex = queue.popleft()
      print(current_vertex)
      for adjacent_vertex in self.graphDict[current_vertex]:
        if adjacent_vertex not in visited:
          visited.add(adjacent_vertex)
          queue.append(adjacent_vertex)


  def DFS(self, vertex):
    visited = set()
    stack = [vertex]
    while stack:
      current_vertex = stack.pop()
      if current_vertex not in visited:
        print(current_vertex)
        visited.add(current_vertex)
      for adjacent_vertex in self.graphDict[current_vertex]:
        if adjacent_vertex not in visited:
          stack.append(adjacent_vertex)
            




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
graph.addVertex("d")
graph.addVertex("e")
graph.addEdge("a", "b")
graph.addEdge("a", "c")
graph.addEdge("b", "e")
graph.addEdge("c", "d")
graph.addEdge("d", "e")


# graph.printGraph()
print("Breadth for search: ")
graph.BFS("a")

print("Depth for search:")
graph.DFS("a")