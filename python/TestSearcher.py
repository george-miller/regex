import graph
from searcher import *

testGraphs = [ 
# [regex, text, matches]
[
	'abc(d|e|f)*', # regex
	'a b c d e f g t s aa abc abcddddabcdef', # text to be searched
	[Found('abc', 21, 24), Found('abcdddd', 25, 32), Found('abcdef', 32, 38)] # matches
],
[
	'(a|b|c)+',
	'    z d g abc', 
	[Found('abc', 10, 13)]
],
[
	'(a|b|c)?zz(x|y|z)*',
	'zz zzyxyzy zxyxy azzyx abzs czz', 
	[Found('zz', 0, 2), Found('zzyxyzy', 3, 10), Found('azzyx', 17, 22),  Found('czz', 28, 31)] 
],
[
	'AB(C|D)?E*',
	'A AB BAC CWWHHA BAACDEEEABCDD BBA PDJKWONRLABKJDFKPWJ ABCEEEEE', 
	[Found('AB', 2, 4), Found('ABC', 24, 27), Found('AB', 43, 45), Found('ABCEEEEE', 54, 62)] 
]
]
def run():
	for test in testGraphs:
		g = graph.createGraph(test[0])
		found = findAll(test[1], g)
		if len(test[2]) != len(found):
			for i in found: print i
			print 
			for i in test[2]: print i
			raise Exception("Expected array of length {0} but got {1}.".format(len(test[2]), len(found)))
		for result in test[2]:
			if not result in found:
				raise Exception("Expected [{0}] in {1}".format(result, [str(s) for s in found]))


if __name__ == '__main__':
	run()