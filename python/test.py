import TestSyntax, TestGraph, TestSearcher
import traceback

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


modulesRunners = [
	TestSyntax.run,
	TestGraph.run,
	TestSearcher.run
]

def run():
	errorCount = 0
	for i in modulesRunners:
		print i.__module__
		try:
			i()
		except Exception as e:
			errorCount += 1
			print "{0}  {1}{2}".format(bcolors.WARNING, 
				traceback.format_exc(), bcolors.ENDC)
		else:
			print "{0}  Passed!{1}".format(bcolors.OKGREEN, bcolors.ENDC)

	if errorCount == 0:
		print "{0}{1} total errors.{2}".format(bcolors.OKGREEN, errorCount, bcolors.ENDC)
	else:
		print "{0}{1} total errors.{2}".format(bcolors.WARNING, errorCount, bcolors.ENDC)


if __name__ == '__main__':
	run()