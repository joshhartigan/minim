# Name:        variables.py
# Author:      Josh Hartigan
# Description: Minim Scripting Language - Variable declaration and control.

import sys

import library
import min_types

varTable = {
    # "identifier": value
}

def declare(line):
    if "var " not in line:
        sys.stdout.write( library.errors["empty_var"] + line + "\n" )
        sys.exit(1)

    line = line.split()

    identifier = line[1]
    value = line[3] # line[2] == "="

    if min_types.string(value):
        varTable[identifier] = min_types.stringValue(value)
    elif min_types.boolean(value):
        varTable[identifier] = min_types.booleanValue(value)
    elif min_types.number(value):
        varTable[identifier] = min_types.numberValue(value)

