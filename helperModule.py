import os
'''
	This module contains functions those have a very high level vision
'''


# for coloring
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def printWarning(string):
	return bcolors.WARNING, bcolors.BOLD, string, bcolors.ENDC

def printFail(string):
	return bcolors.FAIL, bcolors.BOLD, string, bcolors.ENDC

def printSuccess(string):
	return bcolors.OKGREEN, bcolors.BOLD, string, bcolors.ENDC

def printBlue(string):
	return bcolors.OKBLUE, bcolors.BOLD, string, bcolors.ENDC



# for getting file extension (empty string is returned if no extension)
def getFileExtension(target_path):
	# get lower-case path (to be used)
	path_lower = target_path.lower()
	# get extension from lower-case path
	_, resulting_extension = os.path.splitext(path_lower)
	return resulting_extension
