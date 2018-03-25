import sys
import os
import json
from dicttoxml import dicttoxml
from dataSavingModule import *
from helperModule import *
import csv

supportedDataTypes = ["number", "string"]


def validateCMDLineArguments():
	# if length is 2 or less, then you didn't send data types in the CSV file
	# len(sys.argv)
	if len(sys.argv) <= 2:
		print bcolors.FAIL, bcolors.BOLD
		print 'Invalid number of arguments.\nValid way to call main file:', bcolors.ENDC, bcolors.BOLD
		print '>>\tpython main.py transactions.py dataType1 dataType2 dataType3 ...', bcolors.ENDC, bcolors.FAIL, bcolors.BOLD
		print 'where dataType1,2,3 are valid supported data types those map to CSV file fields', bcolors.ENDC
		return -1

	# now validate csv extension file (sent through argv[1])
	# print 'file extension: ', file_extension
	csv_path = sys.argv[1]
	if getFileExtension(csv_path) != '.csv' or not os.path.isfile(csv_path):
		print bcolors.FAIL, bcolors.BOLD
		print 'Only existing CSV files are supported as a second argument!', bcolors.ENDC
		return -1

	# now validate that data sent are supported
	dataType_List = sys.argv[2:]
	# print 'List of data types sent: ', dataType_List

	#iterate and validate each and every one (support validation)
	for dataType in dataType_List:
		if dataType not in supportedDataTypes:
			print bcolors.FAIL, bcolors.BOLD
			print 'There\'s one or more data types that don\'t match the supported data type list', bcolors.ENDC
			print 'Suported data types:\n', supportedDataTypes
			return -1

	# now that all are validated, return 1 for success
	return 1

def validateUTF(dictionary_underInv):
	# coming is a dictionary, get list of values
	listOfValues = dictionary_underInv.values()

	# iterate them and validate row data is UTF-8
	for value in listOfValues:
		try:
			value.decode('utf-8')
			# print "string is UTF-8, length %d bytes" % len(value)
		except UnicodeError:
			print "A string in this row is not UTF-8. Row will be ignored."
			return -1

	# passed test, return 1 for success
	return 1

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def validateDataTypes(dictionary_underInv, dataTypeList_underInv, csv_headers):
	index = 0
	for key in csv_headers:
		# get value mapping to this key, get corresponding data type & validate
		print 'Validating ', dictionary_underInv[key], ' as [', dataTypeList_underInv[index], ']'

		if (dataTypeList_underInv[index] == 'number' and not is_number(dictionary_underInv[key])) or \
			(dataTypeList_underInv[index] == 'string' and not isinstance(dictionary_underInv[key], basestring)):
			print bcolors.FAIL, bcolors.BOLD, \
				'There\'s a variable that doesn\'t match corresponding data type in this row. Row will be ignored.', \
				bcolors.ENDC
			return -1

		index += 1

	# as we got here, return 1 for success
	return 1

print '\n\n'

if __name__ == "__main__":
	# first of all, validate command line arguments
	if validateCMDLineArguments() != -1:
		with open('transactions.csv', 'rb') as csvfile:
			spamreader = csv.DictReader(csvfile)
			# no need to worry about memory limitations as spamreader does a lazy load on the file (line-by-line)
			# first line is the header one
			headers = spamreader.fieldnames

			# iterate rows, validate UTF-8 & data types then append to files (json and xml)
			for row in spamreader:
				# now row is a dictionary of keys (CSV header) and values (excel row) [Blue color]
				print bcolors.OKBLUE, bcolors.BOLD
				print 'Validating row #', spamreader.line_num
				tempReturn = validateUTF(row)
				print bcolors.ENDC

				if tempReturn == 1:
					# then validated row is all UTF-8, now validate data types [red color]
					if validateDataTypes(row, sys.argv[2:], headers) == -1:
						print bcolors.WARNING, bcolors.BOLD, 'Row is being neglected !!!', bcolors.ENDC
					else:
						# inform user that row is ok and ready to save to the files
						print bcolors.OKGREEN, bcolors.BOLD, 'Row is OK and being saved !', bcolors.ENDC
						appendDictToFile(row, 'new.json')
						appendDictToFile(row, 'new.xml')



print '\n\n'
'''
	Unit Tests
'''
