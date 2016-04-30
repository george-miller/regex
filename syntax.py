# Allowed characters are alphanums, +, *, (, ), [, ], {, }, ?, |, -, ',', '\'
def containsBadChars(regex):
	goodChars = ['|', '[', ']', '{', '}', '(', ')', '+', '*', '?', '-', ',', '\\', '.']
	for i in range(len(regex)):
		c = regex[i]
		if regex[i-1] == '\\': continue
		if not c.isalnum() and not c in goodChars:
			return i
	return -1

# Every ( [ { must have a matching } ] )
def allParenMatch(regex):
	foundParens = []
	openers = ['(', '[', '{']
	closers = [')', ']', '}']
	closeToOpen = {}
	for i in range(len(openers)):
		closeToOpen[closers[i]] = openers[i]
	parensSeen = []
	for i in range(len(regex)):
		c = regex[i]
		if i > 0 and regex[i-1] == '\\':
			continue
		if c in openers:
			parensSeen.append(c)
		elif c in closers:
			if closeToOpen[c] in parensSeen:
				parensSeen.remove(closeToOpen[c])
			else:
				return i
	if parensSeen != []:
		return len(regex)
	return -1

# Cannot have negatives in {x,y}, and must be in that form
# [] must be of the form [x-y] and ord(x) <= ord(y)
def legalRange(regex):
	for i in range(len(regex)):
		c = regex[i]
		if c == '{':
			try:
				if ',' in regex[i+1:]:
					# of form {x,y}
					closingCurly = regex[i+1:].index('}') + i+1
					seperator = regex[i+1:closingCurly].index(',') + i+1
					minCanHave = int(regex[i+1:seperator])
					maxCanHave = int(regex[seperator+1:closingCurly])
				elif '}' in regex[i+1:]:
					# of form {x}
					closingCurly = regex[i+1:].index('}') + i+1
					minCanHave = int(regex[i+1:closingCurly])
					maxCanHave = minCanHave+1
				else:
					return i
			except:
				return i
			else:
				if minCanHave < 0:
					return i
				elif maxCanHave < 0 or maxCanHave < minCanHave:
					return i
		elif c == '[':
			try:
				closingIndex = regex[i:].index(']') + i
				hyphenIndex = regex[i:].index('-') + i
			except:
				return i
			if len(regex[i+1:hyphenIndex]) > 1:
				return i
			if len(regex[hyphenIndex+1:closingIndex]) > 1:
				return i
			startChar = regex[i+1:hyphenIndex]
			endChar = regex[hyphenIndex+1:closingIndex]
			if ord(startChar) > ord(endChar):
				return i
	return -1

# '|' must be of the form x|y where x and y could be inside parens or []
# '*', '+', '?', and '|' must come after an alphanum or ), ], }
# {} must come after ) or alphanum
def legalCharPositions(regex):
	for i in range(len(regex)):
		c = regex[i]
		if c == '|' and (i == 0 or i == len(regex)-1): # disallow | at the beginning and end
			return i
		if i > 0 and regex[i-1] == '\\':
			continue
		if c == '*' or c == '+' or c == '?':
			if i > 1 and regex[i-2] == '\\':
				continue
			if i == 0:
				return i
			if not regex[i-1].isalnum() and regex[i-1] not in [')', ']', '}']:
				return i
		elif c == '|':
			if i == 0:
				return i
			if not regex[i-1].isalnum() and regex[i-1] not in [')', ']', '}', '*', '+', '?']:
				return i
		elif c == '{':
			if not regex[i-1].isalnum() and regex[i-1] not in [')', ']']:
				return i
	return -1




# Returns -1 if syntax is ok, and a index 
# (where the error was) if the sytnax is wrong
def test(regex):
	results = [
		containsBadChars(regex), 
		allParenMatch(regex), 
		legalRange(regex),
		legalCharPositions(regex)
	]
	for result in results:
		if result >= 0:
			return result
	
	return -1