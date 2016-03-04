class PyGraph(object):
	
	"creates an empty adjacency list"
	def __init__(self,n):
		self.AdjList = [ [] for i in range(n)]		

	
	"directionally connect A to B"
	def connectAToB(self,v1,v2):
		self.AdjList[v1].append(v2)
	
	"undirectionally connect two nodes"
	def connectNodes(self,v1,v2):
		self.AdjList[v1].append(v2)
		self.AdjList[v2].append(v1)


	"directionally disconnects A from B"
	def disconnectAFromB(self,v1,v2):
		self.AdjList[v2].remove(v1)

	"undirectionally disconnect two nodes"
	def disconnectNodes(self,v1,v2):
		self.AdjList[v1].remove(v2)
		self.AdjList[v2].remove(v1)


	"checks if a connection exists from v1 to v2"
	def isAConnectedToB(self,v1,v2):
		return v2 in self.AdjList[v1]

	"checks if a bidirectional connection exists between v1 and v2"
	def isConnected(self,v1,v2):
		return (v2 in self.AdjList[v1] and v1 in self.AdjList[v2])

	
	"visually displays the state of the graph"
	def printGraph(self):
		for vertex in self.AdjList:
			print(vertex)
