from graphutils import *


def getNextNonEscaped(text, char):
	for i in range(1, len(text)):
		if text[i] == char and text[i-1] != '\\':
			return i
	print "{0} not found in {1}".format(char, text)
	exit(1)

# To accurately get the index of the closing parenthesis, we have 
# to use a stack to find the correct corresponding parenthesis
def getClosingParen(regex, regexIndex):
	stack = []
	for i in range(regexIndex, len(regex)):
		c = regex[i]
		if c == '(':
			stack.append('(')
		elif c == ')':
			if stack.pop() != '(': 
				print "Error, stack did not contain '('"
				exit(1)
			if stack == []:
				return i
				break
	print "Error closing paren not found"
	exit(1)

def parseChunk(regex, regexIndex, g):
	c = regex[regexIndex]
	if c.isalnum():
		n = Node(ord(c))
		g.append(n)
		g.twoPrevOuput = g.prevOutput
		g.prevInput = [n]
		g.prevOutput = [n]
		return regexIndex+1

	elif c == '.':
		a = []
		for i in range(150):
			if chr(i).isalnum():
				a.append(i)
		n = Node(a) # matches all alpha numerics

		g.append(n)
		g.twoPrevOuput = g.prevOutput
		g.prevInput = [n]
		g.prevOutput = [n]
		return regexIndex+1

	elif c == '\\':
		if regex[regexIndex+1] == 's':
			n = Node([ord(' '), ord('\t'), ord('\n')])
		else:
			n = Node(ord(regex[regexIndex+1]))
		g.append(n)
		g.twoPrevOuput = g.prevOutput
		g.prevInput = [n]
		g.prevOutput = [n]
		return regexIndex+2

	elif c == '+':
		for o in g.prevOutput:
			for i in g.prevInput:
				o.edges.append(i)
		return regexIndex+1

	elif c == '*': 
		# Backedge
		for o in g.prevOutput:
			for i in g.prevInput:
				o.edges.append(i)
		# Edge that skips graph
		for o in g.twoPrevOuput:
			g.prevOutput.append(o)
		return regexIndex+1

	elif c == '{':
		closingCurly = getNextNonEscaped(regex[regexIndex:], '}') + regexIndex
		if ',' in regex[regexIndex+1:closingCurly]:
			seperator = regex[regexIndex+1:closingCurly].index(',') + regexIndex+1
			minCanHave = int(regex[regexIndex+1:seperator])
			maxCanHave = int(regex[seperator+1:closingCurly])
		else:
			minCanHave = int(regex[regexIndex+1:closingCurly])
			maxCanHave = minCanHave
		toBeClonedG = Graph(inputNodes=g.prevInput, outputNodes=g.prevOutput)
		# Special behavior if this curly is the first thing in the regex
		if g.twoPrevOuput == g.inputNodes:
			for n in g.prevInput:
				g.twoPrevOuput.remove(n)
		else:
			for n in g.prevInput:
				for o in g.twoPrevOuput:
					o.edges.remove(n)
		
		g.prevInput = []
		g.prevOutput = []

		for amount in range(minCanHave, maxCanHave+1):
			amountG = Graph()
			amountG.inputNodes = []
			amountG.outputNodes = []
			if amount == 0:
				g.prevOutput.extend(g.twoPrevOuput)
				continue
			if amount > 0:
				iGraph = clone(toBeClonedG)
				amountG.inputNodes.extend(iGraph.inputNodes)
				amountG.prevOutput = iGraph.outputNodes
			for i in range(1, amount):
				iGraph = clone(toBeClonedG)
				for n in iGraph.inputNodes:
					amountG.append(n)
				amountG.prevOutput = iGraph.outputNodes


			# Connect the last iGraph's output to amountG's output
			amountG.outputNodes.extend(amountG.prevOutput)

			g.prevInput.extend(amountG.inputNodes)
			g.prevOutput.extend(amountG.outputNodes)
			if g.twoPrevOuput == g.inputNodes:
				g.inputNodes.extend(amountG.inputNodes)
			else:
				for n in g.twoPrevOuput:
					n.edges.extend(amountG.inputNodes)

		return closingCurly+1

	elif c == '[': 
		closingIndex = regex[regexIndex:].index(']') + regexIndex
		hyphenIndex = regex[regexIndex:].index('-') + regexIndex
		n = Node(range(ord(regex[hyphenIndex-1]), ord(regex[hyphenIndex+1])+1))
		g.append(n)
		g.twoPrevOuput = g.prevOutput
		g.prevInput = [n]
		g.prevOutput = [n]
		return closingIndex+1

	elif c == '|':
		g.outputNodes.extend(g.prevOutput)
		g.prevOutput = [] # Go back to start
		g.twoPrevOuput = []
		g.prevInput = []
		return regexIndex+1

	elif c == '(':
		closingIndex = getClosingParen(regex, regexIndex)

		# closingIndex = regex[regexIndex:].index(')')+regexIndex # Guarenteed by syntax checker to find ')'
		innerG = createGraph(regex[regexIndex+1:closingIndex])
		g.twoPrevOuput = g.prevOutput[:]
		for o in g.prevOutput:
			o.edges.extend(innerG.inputNodes)
		if g.prevOutput == []:
			g.inputNodes.extend(innerG.inputNodes)
		g.prevOutput = innerG.outputNodes
		g.prevInput = innerG.inputNodes
		
		return closingIndex+1
	
	elif c == '?':
		if g.twoPrevOuput != []:
			g.prevOutput.extend(g.twoPrevOuput)
			return regexIndex+1
		else:
			# ? at start of regex
			regexIndex = parseChunk(regex, regexIndex+1, g)
			for n in g.prevInput:
				g.inputNodes.append(n)
			return regexIndex
		
		
	else:
		print "ERROR: Unexpected c="+str(c)
		exit(1)

def createGraph(regex):
	g = Graph()

	regexIndex = 0
	while regexIndex < len(regex):
		regexIndex = parseChunk(regex, regexIndex, g)

	if g.inputNodes == []:
		g.inputNodes.extend(g.prevInput)

	g.outputNodes.extend(g.prevOutput)
	return g

