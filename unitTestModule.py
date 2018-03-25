import sys
import os
import json
from dicttoxml import dicttoxml
from dataSavingModule import *
from helperModule import *
from main import *


def sweetSpot_UT():
	# (Orange & Bold)
	print bcolors.WARNING, bcolors.BOLD
	print '**************************'
	print 'Begin: Testing "sweetSpot"'
	print '**************************\n', bcolors.ENDC
	
	# initializations
	tempFileJSON = open("testFile.json", "r+")
	tempFileXML = open("testFile.xml", "r+")


	# First test (Green & Bold)
	print 'Test #1'
	print '************', bcolors.OKBLUE, bcolors.BOLD
	print 'Arguments sent:\n\tfile object: the one named "file.json"\n'
	print 'Expected return: int: larger than 0'
	# Function calls & Results
	tempReturn = sweetSpot(tempFileJSON, False)
	print 'The sweet spot (actual return): ',tempReturn
	if tempReturn > 0:
		print 'Status: ', bcolors.OKGREEN, bcolors.BOLD, 'OK', bcolors.ENDC
	else:
		print 'Status: ', bcolors.FAIL, bcolors.BOLD, 'Fail', bcolors.ENDC
	print '************'
	print 'End: Test #1\n\n'


	# Second test (Red & Bold)
	print 'Test #2'
	print '************', bcolors.OKBLUE, bcolors.BOLD
	print 'Arguments sent:\n\tfile object: inappropriate value\n'
	print 'Expected return: int: -1'
	# Function calls & Results
	tempReturn = sweetSpot("bad argument", False)
	print 'The sweet spot (actual return): ',tempReturn
	if tempReturn == -1:
		print 'Status: ', bcolors.OKGREEN, bcolors.BOLD, 'OK', bcolors.ENDC
	else:
		print 'Status: ', bcolors.FAIL, bcolors.BOLD, 'Fail', bcolors.ENDC
	print '************'
	print 'End: Test #2\n\n'


	# Third test (Red & Bold)
	print 'Test #3'
	print '************', bcolors.OKBLUE, bcolors.BOLD
	print('Arguments sent:\n\tfile object: inappropriate value\n')
	print('Expected return: int: larger than 0')
	# Function calls & Results
	tempReturn = sweetSpot(tempFileXML, False)
	print 'The sweet spot (actual return): ',tempReturn
	if tempReturn > 0:
		print 'Status: ', bcolors.OKGREEN, bcolors.BOLD, 'OK', bcolors.ENDC
	else:
		print 'Status: ', bcolors.FAIL, bcolors.BOLD, 'Fail', bcolors.ENDC
	print '************'
	print 'End: Test #3\n\n'

	tempFileJSON.close()
	tempFileXML.close()

	# (Orange & Bold)
	print bcolors.WARNING, bcolors.BOLD
	print '**************************'
	print 'End: Testing "sweetSpot"'
	print '**************************\n', bcolors.ENDC

sweetSpot_UT()


def appendDictToFile_UT():
	# (Orange & Bold)
	print bcolors.WARNING, bcolors.BOLD
	print '*******************************'
	print 'Begin: Testing "appendDictToFile"'
	print '*******************************\n', bcolors.ENDC

	nonExistingJSONPath = 'nonexisting.json'
	nonExistingXMLPath = 'nonexisting.xml'

	#initializations
	sampleDictionary = {
		'id': 5,
		'name': 'Moustafa'
	}

	# deleting files if they exist (to test the non-existing files handling)
	if os.path.isfile(nonExistingJSONPath):
		os.remove(nonExistingJSONPath)

	if os.path.isfile(nonExistingXMLPath):
		os.remove(nonExistingXMLPath)


	# First test (Green & Bold)
	print 'Test #1'
	print '************', bcolors.OKBLUE, bcolors.BOLD
	print 'Arguments sent:\n\tdict: sample valid dictionary\n\tstring: path to a non-existing json file named "',nonExistingJSONPath,'"\n'
	print 'Expected return: int: larger than 0 & a new file of the name specified is created with valid data inside'
	# Function calls & Results
	tempReturn = appendDictToFile(sampleDictionary, nonExistingJSONPath)
	print 'Function returned: ',tempReturn
	if tempReturn > 0:
		print 'Status: ', bcolors.OKGREEN, bcolors.BOLD, 'OK', bcolors.ENDC
	else:
		print 'Status: ', bcolors.FAIL, bcolors.BOLD, 'Fail', bcolors.ENDC
	print '************'
	print 'End: Test #1\n\n'


	# Second test (Green & Bold)
	print 'Test #2'
	print '************', bcolors.OKBLUE, bcolors.BOLD
	print 'Arguments sent:\n\tdict: sample valid dictionary\n\tstring: path to a non-existing xml file named "',nonExistingXMLPath,'"\n'
	print 'Expected return: int: larger than 0 & a new file of the name specified is created with valid data inside'
	# Function calls & Results
	tempReturn = appendDictToFile(sampleDictionary, nonExistingXMLPath)
	print 'Function returned: ',tempReturn
	if tempReturn > 0:
		print 'Status: ', bcolors.OKGREEN, bcolors.BOLD, 'OK', bcolors.ENDC
	else:
		print 'Status: ', bcolors.FAIL, bcolors.BOLD, 'Fail', bcolors.ENDC
	print '************'
	print 'End: Test #2\n\n'


	# Third test (Green & Bold)
	print 'Test #3'
	print '************', bcolors.OKBLUE, bcolors.BOLD
	print 'Arguments sent:\n\tdict: invalid dictionary value\n\tstring: path to an existing file (a don\'t-care value)\n'
	print 'Expected return: int: -1, no edits were done on the file from previous tests (they still have one object)'
	# Function calls & Results
	tempReturn = appendDictToFile("invalidDictionary", nonExistingXMLPath)
	print 'Function returned: ',tempReturn
	if tempReturn == -1:
		print 'Status: ', bcolors.OKGREEN, bcolors.BOLD, 'OK', bcolors.ENDC
	else:
		print 'Status: ', bcolors.FAIL, bcolors.BOLD, 'Fail', bcolors.ENDC
	print '************'
	print 'End: Test #3\n\n'


	# Forth test (Green & Bold)
	print 'Test #4'
	print '************', bcolors.OKBLUE, bcolors.BOLD
	print 'Arguments sent:\n\tdict: sample valid dictionary\n\tstring: path to an existing json file named "',nonExistingJSONPath,'"\n'
	print 'Expected return: int: larger than 0 & the old file of the name specified is appended with the same data as before (duplicated object)'
	# Function calls & Results
	tempReturn = appendDictToFile(sampleDictionary, nonExistingJSONPath)
	print 'Function returned: ',tempReturn
	if tempReturn > 0:
		print 'Status: ', bcolors.OKGREEN, bcolors.BOLD, 'OK', bcolors.ENDC
	else:
		print 'Status: ', bcolors.FAIL, bcolors.BOLD, 'Fail', bcolors.ENDC
	print '************'
	print 'End: Test #4\n\n'


	# Fifth test (Green & Bold)
	print 'Test #5'
	print '************', bcolors.OKBLUE, bcolors.BOLD
	print 'Arguments sent:\n\tdict: sample valid dictionary\n\tstring: path to an existing xml file named "',nonExistingXMLPath,'"\n'
	print 'Expected return: int: larger than 0 & the old file of the name specified is appended with the same data as before (duplicated object)'
	# Function calls & Results
	tempReturn = appendDictToFile(sampleDictionary, nonExistingXMLPath)
	print 'Function returned: ',tempReturn
	if tempReturn > 0:
		print 'Status: ', bcolors.OKGREEN, bcolors.BOLD, 'OK', bcolors.ENDC
	else:
		print 'Status: ', bcolors.FAIL, bcolors.BOLD, 'Fail', bcolors.ENDC
	print '************'
	print 'End: Test #5\n\n'


	# (Orange & Bold)
	print bcolors.WARNING, bcolors.BOLD
	print '*******************************'
	print 'End: Testing "appendDictToFile"'
	print '*******************************\n', bcolors.ENDC

appendDictToFile_UT()

def validateCMDLineArguments_UT():
	# (Orange & Bold)
	print bcolors.WARNING, bcolors.BOLD
	print '**************************'
	print 'Begin: Testing "validateCMDLineArguments"'
	print '**************************\n', bcolors.ENDC

	tempReturn = validateCMDLineArguments()
	print bcolors.OKBLUE, bcolors.BOLD
	print 'Expected return: 1 if valid arguments and -1 otherwise'
	print 'Actual return: ', tempReturn, bcolors.ENDC

	# (Orange & Bold)
	print bcolors.WARNING, bcolors.BOLD
	print '**************************'
	print 'End: Testing "validateCMDLineArguments"'
	print '**************************\n', bcolors.ENDC

# validateCMDLineArguments_UT()