#!/usr/bin/python

# Name:        minim.py
# Author:      Josh Hartigan
# Description: Minim Scripting Language - Read file, process lines.

from sys import argv

import functions

def main():
    source = open(argv[1], "r")

    for line in source.readlines():
        process(line)

def process(line):
    # line is function call?
    if line[0] == "(" and line[ len(line) - 2 ] == ")":
        functions.processCaller(line)

if __name__ == "__main__":
    main()
