#!/usr/bin/env python

""" Make a specified number of junk files in a directory of your choosing.
    There is no default directory--that has to be specified.
    The default number of files is 10. If you don't specify, you get 10 files.

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
    try:  
        os.mkdir(directory)
        print "Now directory exists!"
    except:
        sys.exit("Invalid directory structure, not cool. Exiting.")
        
try:
    number = sys.argv[2]
except IndexError:
    number = 10

filename = "roboto.txt"

fully_specified_file = os.path.join(directory, filename)

os.system("touch " + fully_specified_file)