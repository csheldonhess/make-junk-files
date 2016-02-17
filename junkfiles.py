#!/usr/bin/env python

""" Make a specified number of junk files in a directory of your choosing.
    There is no default directory--that has to be specified.
    The default number of files is 100. If you don't specify, you get 100 files.

usage: ./junkfiles.py directory number_of_files
       ./junkfiles.py junkfiledir 100

"""


import sys
import os
import random
import math

try:
    if sys.argv[ 1 ] == 'help' or sys.argv[ 1 ] == '--help' or sys.argv[ 1 ] == '-h':
        usage()
except IndexError:
    usage()

directory = sys.argv[1]

if os.path.exists(directory):
    print "You chose an existing directory: " + directory + "\n Continue?"
    yn = raw_input("Yes (Y) or No (N): ")
    if not (yn.lower() == 'y' or yn.lower() == 'yes'):
        sys.exit("No problem. Try again.")
else:
    print "Continuing..."
    try:  
        os.mkdir(directory)
        print "Now directory exists!"
    except:
        sys.exit("Invalid directory structure, not cool. Exiting.")
        
try:
    number = sys.argv[2]
except IndexError:
    number = 10

try:
    number_of_files = int(number)
    if number_of_files <= 0:
        print "Negative number? Nice try. You're getting 100 files, then; deal with it."
        number_of_files = 100
except ValueError:
    print "That wasn't a number. You're getting 100 files."
    number_of_files = 100

extensions = [".txt", ".csv", ""] 
junky_stuff = ["-", "_", "+", "-", "_"]
words = ["programs", "events", "images", "speakers", "keynotes", "slides", "organizers", "locations", "misc"]
years = range(2006, 2016)


for filenumber in range(0, number_of_files):
    wi = filenumber % len(words)
    yi = filenumber % len(years)
    if filenumber % 2 == 0:
        filename = "code4lib" + random.choice(junky_stuff) + words[wi] + random.choice(junky_stuff) + str(years[yi]) + random.choice(extensions)
    else:
        filename = "code4lib" + random.choice(junky_stuff) + str(years[yi]) + random.choice(junky_stuff) + words[wi] + random.choice(extensions)

    fully_specified_file = os.path.join(directory, filename)
    os.system("touch " + fully_specified_file)

print "Complete."