import syntax
import graph
import searcher

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def compile(regex):
	result = syntax.test(regex)
	if result >= 0:
		print "{0}{1}{2}{3}".format(regex[:result], bcolors.FAIL, regex[result:], bcolors.ENDC)
		print "regex.compile: Error at index " + str(result)
		return None
	else:
		return graph.createGraph(regex)

def findall(text, g):
	if not isinstance(g, graph.Graph):
		raise Exception("The given graph was not a graph")
	return searcher.findAll(text, g)


