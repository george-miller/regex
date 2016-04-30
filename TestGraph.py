from graphutils import *
from graph import *

def testClone():
	g = Graph()
	a = Node(ord('a'))
	g.inputNodes.append(a)
	b = Node(ord('b'))
	a.edges.append(b)
	g.outputNodes.append(b)
	g.outputNodes.append(a)
	b.edges.append(b)
	r = str(g)

	cloneG = clone(g)
	c = str(cloneG)
	if r != c:
		raise Exception("expected:\n{0}\ngot\n{1}".format(r, c))

	g = Graph()
	a = Node(ord('a'))
	g.inputNodes.append(a)
	b = Node(ord('b'))
	c = Node(ord('c'))
	g.inputNodes.append(b)
	g.inputNodes.append(c)
	b.edges.append(c)
	a.edges.append(c)
	c.edges.append(a)
	b.edges.append(b)
	g.outputNodes.append(c)

	r = str(g)

	cloneG = clone(g)
	c = str(cloneG)
	if r != c:
		raise Exception("expected:\n{0}\ngot\n{1}".format(r, c))

	a = Node(ord('a'))
	g = Graph(inputNodes=[a], outputNodes=[a])
	cloneG = clone(g)
	# print cloneG.startNode.matches
	for i in range(len(g.inputNodes)):
		assert g.inputNodes[i].matches == cloneG.inputNodes[i].matches


def testCurly():
	a = Node(ord('a'))
	a1 = Node(ord('a'))
	a2 = Node(ord('a'))
	g = Graph()
	# 1
	g.inputNodes.append(a)
	g.outputNodes.append(a)
	# 2
	g.inputNodes.append(a1)
	a1.edges.append(a2)
	g.outputNodes.append(a2)

	expected = str(g)

	real = createGraph('a{0,2}')
	r = str(real)

	if r != expected:
		raise Exception("expected:\n{0}\ngot\n{1}".format(expected, r))

def testParenOr():
	expected = (
	"Node matches a END\n"
	"Node matches b\n"
	"  Node matches c END\n"
	"Node matches d END\n"
	)

	g = createGraph('a|(bc|d)')
	s = str(g)
	if s != expected:
		raise Exception("expected:\n{0}\ngot\n{1}".format(expected, s))


def testOr():
	expected = (
	"Node matches a END\n"
	"Node matches b\n"
	"  Node matches c END\n"
	"Node matches d END\n"
	)

	g = createGraph('a|bc|d')
	s = str(g)
	if s != expected:
		raise Exception("expected:\n{0}\ngot\n{1}".format(expected, s))


def testPlusAndStar():
	expected = (
	"Node matches a\n"
	"  Node matches ['b', 'c', 'd', 'e', 'f']\n"
	"    BackEdge to Node matches ['b', 'c', 'd', 'e', 'f']\n"
	"    Node matches d END\n"
	"      BackEdge to Node matches d\n"
	"  Node matches d END\n"
	"    BackEdge to Node matches d\n"
  	)
	g = createGraph('a[b-f]*d+')
	s = str(g)
	if s != expected:
		raise Exception("expected:\n{0}\ngot\n{1}".format(expected, s))


def testSquareParenPulAndStar():
	expected = (
"Node matches a\n"
"  Node matches ['b', 'c', 'd', 'e', 'f']\n"
"    BackEdge to Node matches ['b', 'c', 'd', 'e', 'f']\n"
"    Node matches c END\n"
"      BackEdge to Node matches c\n"
"      Node matches d END\n"
"        BackEdge to Node matches c\n"
"        BackEdge to Node matches d\n"
"    Node matches d END\n"
"      Node matches c END\n"
"        BackEdge to Node matches c\n"
"        BackEdge to Node matches d\n"
"      BackEdge to Node matches d\n"
"  Node matches c END\n"
"    BackEdge to Node matches c\n"
"    Node matches d END\n"
"      BackEdge to Node matches c\n"
"      BackEdge to Node matches d\n"
"  Node matches d END\n"
"    Node matches c END\n"
"      BackEdge to Node matches c\n"
"      BackEdge to Node matches d\n"
"    BackEdge to Node matches d\n"
	)

	g = createGraph('a[b-f]*(c|d)+')
	s = str(g)
	if s != expected:
		raise Exception("expected:\n{0}\ngot\n{1}".format(expected, s))


def testQuestion():
	expected = (
"Node matches a END\n"
"  Node matches b END\n"
"  Node matches c END\n"
	)

	g = createGraph('a(b|c)?')
	s = str(g)
	if s != expected:
		raise Exception("expected:\n{0}\ngot\n{1}".format(expected, s))


def testEscape():
	expected = (
"Node matches a\n"
"  Node matches +\n"
"    Node matches b END\n"
    )
	g = createGraph('a\\+b')
	s = str(g)
	if s != expected:
		raise Exception("expected:\n{0}\ngot\n{1}".format(expected, s))


def run():
	testClone()
	testCurly()
	testOr()
	testParenOr()
	testPlusAndStar()
	testSquareParenPulAndStar()
	testQuestion()
	testEscape()
	
if __name__ == '__main__':
	run()