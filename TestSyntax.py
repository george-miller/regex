import syntax

#  -------
# | RULES |
#  -------
# Every ( [ { must have a matching } ] )
# Cannot have negatives in {x,y}
# [] must be of the form [x-y] and ord(x) <= ord(y)
# '|' must be of the form x|y where x and y could be inside parens or []
# Allowed characters are alphanums, +, *, (, ), [, ], {, }, ?, |, -

falseCases = [
	('abc(()', 6),
	('bcdef)', 5),
	('*abd', 0),
	('+abd', 0),
	('((\))))', 6),
	('{}{}', 0),
	('[][]', 0),
	('?fdas', 0),
	('a|d|', 3) ,
	('ab{-1,-2}', 2),
	('d[ax-ds]fdas', 1),
	('@$%#!(VCX', 0)
]

trueCases = [
	"ab|c|d",
	"ab{2}",
	"ab{1,4}",
	'abc{111}',
	"t[r-w]he",
	"t(f|ew|d)*",
	"t(fdsa)+",
	"hjmkls",
	"hello?"
]

badCharTests = [
	('webjkfsdsjk()*', -1),
	('{}[]{}()', -1),
	('$*!&', 0),
	('jsnel^', 5),
	('nekx__', 4),
	('jes*+', -1)
]

parensMatchTests = [
	('()()', -1),
	('))((', 0),
	('][', 0),
	('([])', -1),
	('[{}', 3),
	('([{}])', -1),
	('[{(}]', 5),
	('[{(}])', -1),
	('([{}\]])', -1)
]

legalRangeTests = [
	('a{0,3}', -1),
	('[8-0]', 0),
	('nks[-1-6]', 3),
	('(a){-1,8}', 3),
	('[\w-p]', 0),
	('[aa-ab]', 0),
]

legalCharPositionsTests = [
	('{0-3}', 0),
	('(as){0-3}', -1),
	('+*(saf)', 0),
	('(fdsa)*', -1),
	('fdas+', -1),
	('\++', -1),
]

def testTrueCases():
	for case in trueCases:
		result = syntax.test(case)
		if result >= 0:
			raise Exception("Expected {0} to return -1, instead it returned {1}".format(case, result))


def testFalseCases():
	for case in falseCases:
		result = syntax.test(case[0])
		if result < 0:
			raise Exception("Expected {0} to return false, instead it was {1}".format(case[0], result))
		else:
			if result != case[1]:
				raise Exception("regex:{0} Expected error at "\
					"{1} but got {2}".format(case[0], case[1], result))

def testSubmethods():
	data = [
		badCharTests,
		parensMatchTests,
		legalRangeTests,
		legalCharPositionsTests
	]
	methods = [
		syntax.containsBadChars,
		syntax.allParenMatch,
		syntax.legalRange,
		syntax.legalCharPositions
	]
	for i in range(len(data)):
		for j in range(len(data[i])):
			result = methods[i](data[i][j][0])
			if result != data[i][j][1]:
				raise Exception("Expected {0} for {1} but was {2}".format(data[i][j][1], data[i][j][0], result))
def run():
	testTrueCases()
	testFalseCases()
	testSubmethods()

if __name__ == '__main__':
	run()