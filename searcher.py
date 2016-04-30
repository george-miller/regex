

class Found():
	def __init__(self, text, start, end):
		self.text = text
		self.start = start
		self.end = end

	def __str__(self):
		return "Found {0} beginning at {1} ending at {2}".format(self.text, self.start, self.end)

	def __eq__(self, other):
		return self.text == other.text and self.start == other.start and self.end == other.end

def findRec(outputNodes, text, startIndex, index, n):
	if index < len(text) and n.match(text[index]):
		for edge in n.edges:
			result = findRec(outputNodes, text, startIndex, index+1, edge)
			if result != None:
				return result
		# By putting this after the loop, we guarentee to get the 
		# most specific match, not the most general
		if n in outputNodes:
			return Found(text[startIndex:index+1], startIndex, index+1)

def find(text, g):
	index = 0
	for n in g.inputNodes:
		result = findRec(g.outputNodes, text, 0, index, n)
		if result != None:
			return result

def findAll(text, g):
	found = []
	for i in range(len(text)):
		result = find(text[i:], g)
		if result != None:
			result.start += i
			result.end += i
			found.append(result)
	return found