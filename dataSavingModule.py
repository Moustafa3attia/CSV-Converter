import sys
import os
import json
from dicttoxml import dicttoxml

# Future work: imports are decided upon coming command line arguments
# Future work: check for file read/write permissions

'''
Parameters:
	1. source dictionary (the one to be saved to the file)
	2. JSON file path

Functionality:
	appends coming dictionary to that file in suitable format

Return:
	True for success
	False for failure

Extensions supported:
	1. json
	2. xml
'''

def appendDictToFile(src_dict={}, file_path=""):

	# get lower-case path (to be used)
	path_lower = file_path.lower()
	# get extension from lower-case path
	_, target_extension = os.path.splitext(path_lower)

	if not isinstance(src_dict, dict):
		print 'Function appendDictToFile received a non-dictionary type variable\n'
		return -1

	#If file doesn't exist, 
	if not os.path.isfile(file_path):
		# create one
		file = open(file_path, "w+")


		#write to file depending on extension
		if target_extension == '.json':
			file.write(json.dumps([src_dict]))

		elif target_extension == '.xml':
			file.write(dicttoxml([src_dict]))

		else:
			print "File extension not supported yet !"
			file.close()
			return 0

		# and we're done for this case
		file.close()
		return 1

	#else (file exists)
	file = open(file_path, "r+")


	#go to the sweet spot
	sweetSpot(file, target_extension)

	#and then append with format depending on extension
	if target_extension == '.json':
		file.write(',' + json.dumps(src_dict)+']')

	elif target_extension == '.xml':
		file.write(dicttoxml({'item': src_dict}, root=False)+ '</root>')

	else:
		print "File extension not supported yet !"
		file.close()
		return 0

	file.close()
	return 1

'''
Parameters:
	1. open file object
	2. extension type
	3. optional boolean for file truncate (default: True) > Added for testability

Functionality:
	moves writing cursor to sweet spot (where we should append new object)

Return:
	NULL

Extensions supported:
	1. json
	2. xml
'''

def sweetSpot(file="", truncate=True):

	# as there has to be a file object sent, let's validate that
	# and as there has to be a valid extension sent, let's validate that as well
	if not hasattr(file, 'read'):
		print('Invalid file object was sent to "sweetSpot" function\n')
		return -1

	# get lower-case path (to be used)
	base_name = os.path.basename(file.name)
	# get extension from lower-case path
	_, target_extension = os.path.splitext(base_name)

	#Move the pointer (similar to a cursor in a text editor) to the end of the file. 
	file.seek(0, os.SEEK_END)

	#This code means the following code skips the very last character in the file - 
	#i.e. in the case the last line is null we delete the last line 
	#and the penultimate one
	pos = file.tell()

	#Read each character in the file one at a time from the penultimate 
	#character going backwards, searching for a newline character
	#If we find a new line, exit the search

	file.seek(0, os.SEEK_END)
	pos = file.tell()

	if(target_extension == ".json"):
		while pos > 0 and file.read(1) != "]":
			pos -= 1
			file.seek(pos, os.SEEK_SET)

		#So long as we're not at the start of the file, delete all the characters ahead of this position
		if pos > 0:
			file.seek(pos, os.SEEK_SET)
			if truncate:
				file.truncate()
			return pos
		#else, then we reached file start and it's not a valid move
		else:
			return -1


	elif(target_extension == ".xml"):
		while pos > 0 and file.read(1) != "<":
			pos -= 1
			file.seek(pos, os.SEEK_SET)

		if pos > 0:
			file.seek(pos, os.SEEK_SET)
			if truncate:
				file.truncate()
			return pos
		else:
			return -1

	return 0