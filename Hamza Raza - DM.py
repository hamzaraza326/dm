from collections import defaultdict
class Graph:
 
    def __init__(self,vertices):
        
        self.V= vertices


        self.graph= defaultdict(list)
 
        # To store transitive closure
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def DFSUtil(self,s,visited, matrix):
      visited[s] = True
      for c in self.graph[s]:
        matrix[s][c] = 1
        if visited[c] == False:
          self.DFSUtil(c, visited, matrix)
        elif visited[c] == True:
          for i in range(self.V):
            if matrix[s][i] == 1:
              matrix[c][i] = 1
        for i in range(self.V):
          if matrix[c][i] == 1:
            matrix[s][i] = 1
      return

    def transitiveClosure(self):
      matrix = [[0 for j in range(self.V)] for i in range(self.V)]
      visited = [False]*self.V
      
      for v in self.graph.keys():
        if visited[v] == False:
          self.DFSUtil(v, visited, matrix)
      
      return matrix

# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(2, 0)
g.addEdge(0, 2)
g.addEdge(3, 1)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(3, 2)
 
print ("Transitive closure matrix is")
print (g.transitiveClosure())
