#!/usr/bin/python

# Name:        minim.py
# Author:      Josh Hartigan
# Description: Minim Scripting Language - Read file, process lines.

import sys
import os.path

import functions
import library
import min_types
import variables

def main():
    if not os.path.isfile( sys.argv[1] ):
        sys.stdout.write(library.errors["no_file"] + sys.argv[1] + "\n")
        sys.exit(1)

    if not sys.argv[1].endswith(".min"):
        sys.stdout.write(library.warnings["extension"] + sys.argv[1] + "\n")

    source = open( sys.argv[1], "r" )

    for line in source.readlines():
        process(line)

def process(line):
    # line is function call?
    if min_types.call(line):
        functions.processCaller(line)
    elif min_types.declaration(line):
        variables.declare(line)

if __name__ == "__main__":
    main()
