import regex

# This exp is from hw2
exp = (
'(\$([0-9]+\,)*([0-9]+)\.[0-9]+)' # Dollar amounts like $1,112.30
'|'
'('  # Dollar amounts using words
	'(' # Specifies an amount
		'(' # Amount identifiers
			'(\$)?([0-9]+\,)*([0-9]+)'
			'|'
			'(a|one|two|three|four|five|six|seven|eight|nine)'
		')\s*'
		'(' # Identifier helpers
			'(hundred|thousand|million|billion|trillion|gazillion)(s(\sof)?)?\s*'
		'){0,2}'
	')'
	'(dollar(s)?|buck(s)?)\s*' # Words for units of money
	'(and\s*[0-9]*\s*cent(s)?)?' # Possibly with cents
')'
)

a = regex.compile(exp)
text = open("/Users/gmmotto/repos/nlp/hw2/test_dollar_phone_corpus.txt").read()
b = regex.findall(text, a)

for i in b: print i.text

# diff <(cat hw2_dollar_output.txt) <(python demo.py)