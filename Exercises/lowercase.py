#!/usr/bin/env python

"""
A filter that converts all letters to lowercase.
"""

import fileinput


def convert(line):
    """For each line of input, set all characters to lowercase."""
    print(line.lower().strip())

for line in fileinput.input():
    convert(line)
