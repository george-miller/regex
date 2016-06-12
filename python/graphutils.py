class Node():
	def __init__(self, matches):
		self.matches = matches # list of ints or singular int, corresponds to character codes
		self.edges = [] # list of nodes

	def __str__(self):
		if isinstance(self.matches, list):
			m = [chr(i) for i in self.matches]
			return "Node matches " + str(m)
		elif isinstance(self.matches, int):
			return "Node matches " + str(chr(self.matches))
		else:
			print "Error unexpected when printing Node"
			exit(1)

	def match(self, i):
		if isinstance(self.matches, list):
			if ord(i) in self.matches:
				return True
			else:
				return False
		elif isinstance(self.matches, int):
			if ord(i) == self.matches:
				return True
			else:
				return False
		else:
			print "ERROR: Unexpected matches attribute on node. matches=" + \
				str(self.matches) + " of type=" + str(type(self.matches))
			exit(1)

class Graph():
	def __init__(self, inputNodes=None, outputNodes=None):
		if inputNodes == None:
			self.inputNodes = []
			self.twoPrevOutput = self.inputNodes
			self.prevInput = self.inputNodes
			self.prevOutput = self.inputNodes
		else:
			self.inputNodes = inputNodes
			self.twoPrevOutput = self.inputNodes
			self.prevInput = self.inputNodes
			self.prevOutput = self.inputNodes
		if outputNodes == None:
			self.outputNodes = []
		else:
			self.outputNodes = outputNodes

	def append(self, other):
		if self.prevOutput == []:
			self.inputNodes.append(other)
		else:
			for n in self.prevOutput:
				n.edges.append(other)

	def __str__(self):
		s = ""
		for i in self.inputNodes:
			s += getTreeString(self.outputNodes, i)
		return s

def printTree(endNodes, pathLists, pathIndex, stem, node, s):
	if id(node) in pathLists[pathIndex]:
		s.append(stem  + 'BackEdge to ' + str(node) + '\n')
	else:
		pathLists[pathIndex].append(id(node))
		if node in endNodes:
			s.append(stem + str(node) + ' END\n')
		else:
			s.append(stem + str(node) + '\n')
		pathIndexs = [0]
		for i in range(1, len(node.edges)):
			pathLists.append(pathLists[pathIndex][:])
			pathIndexs.append(len(pathLists)-1 - pathIndex)
		for i in range(len(node.edges)):
			printTree(endNodes, pathLists, pathIndex + pathIndexs[i], "  " + stem, node.edges[i], s)

def getTreeString(endNodes, startNode):
	s = []
	printTree(endNodes, [[]], 0, "", startNode, s)
	return "".join(s)

def cloneRec(nodeMap, clonePrev, realCurrent):
	if realCurrent in nodeMap.keys():
		clonePrev.edges.append(nodeMap[realCurrent])
	else:
		cloneCur = Node(realCurrent.matches)
		nodeMap[realCurrent] = cloneCur
		clonePrev.edges.append(cloneCur)
		for n in realCurrent.edges:
			cloneRec(nodeMap, cloneCur, n)

def clone(g):
	nodeMap = {}
	cloneInputs = []
	for i in g.inputNodes:
		cloneInputs.append(Node(i.matches))
		nodeMap[i] = cloneInputs[-1]
	cloneG = Graph(inputNodes=cloneInputs)
	cloneG.outputNodes = []
	for n in g.inputNodes:
		for i in n.edges:
			cloneRec(nodeMap, nodeMap[n], i)
	for o in g.outputNodes:
		cloneG.outputNodes.append(nodeMap[o])
	return cloneG
