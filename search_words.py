#!/usr/bin/env python

"""
A filter that outputs all full words.
"""

import fileinput
import re

def process(line):
    """For each line of input, extract full words."""
    
    line = re.sub('\W+',' ',line) # Replace any non-alphanumeric characters such as periods or hyphens with spaces
    words = line.split() # Split line into words
    for word in words:
        print(word)
        


for line in fileinput.input(openhook = fileinput.hook_encoded("latin-1")): # latin-1 encoding is needed to read some of the text file names 
    process(line)
