#!/usr/bin/env python

""" make a specified number of junk files 
    in a directory of your choosing

usage: ./junkfiles.py directory number_of_files
	   ./junkfiles.py junkfiledir 100

"""


import sys
import os


try:
    if sys.argv[ 1 ] == 'help' or sys.argv[ 1 ] == '--help' or sys.argv[ 1 ] == '-h':
        usage()
except IndexError:
    usage()

directory = sys.argv[1]

if os.path.exists(directory):
    print "Directory exists"
else: 
	os.mkdir(directory)
	print "Now directory exists!"

try:
	number = sys.argv[2]
except IndexError:
	number = 10

#os.system("touch filename.extension")