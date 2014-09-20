# Name:        library.py
# Author:      Josh Hartigan
# Description: Minim Scripting Language - Standard library definitions.

import sys

import min_types
import variables

errors = {
    "no_file":   "*** Specified source file is non-existant: ",
    "not_found": "*** Specified identifier doesn't exist: ",
    "empty_var": "*** No name or value given in declaration: ",
    "type":      "*** Invalid type as argument: "
}

warnings = {
    "extension": "--> Source file should end in .min: "
}

def write(args):
    values = []

    inString = False
    inCall = False

    for arg in args:
        if arg[0] == "\"" and not min_types.string(arg): # e.g. "Hello
            inString = True
            values.append( min_types.stringValue(arg) )

        elif arg[ len(arg) - 1 ] == "\"" and not min_types.string(arg): # e.g. World"
            inString = False
            values.append( min_types.stringValue(arg) )

        elif not min_types.string(arg) and inString: # Non-quoted, while in a string
            values.append(arg)

        elif min_types.string(arg): # e.g. "Minim"
            values.append( min_types.stringValue(arg) )

        elif min_types.number(arg): # e.g. 345.234
            values.append( min_types.numberValue(arg) )

        elif arg in variables.varTable.keys(): # e.g. myVariableName
            values.append( str(variables.varTable[arg]) )

        else:
            sys.stdout.write( errors["not_found"] + arg + "\n" )
            sys.exit(1)

    sys.stdout.write(" ".join(values))

def writeln(args):
    write(args)
    sys.stdout.write("\n")

# mathematical functions
def plus(args):
    result = 0
    for arg in args:
        if not min_types.number(arg):
            sys.stdout.write( errors["type"] + arg + "\n" )
            sys.exit(1)

        result += min_types.numberValue(arg)

def minus(args):
    if not min_types.number( args[0] ):
        sys.stdout.write( errors["type"] + arg + "\n" )
        sys.exit(1)

    result = min_types.number( args[0] )

    for arg in args[1:]:
        if not min_types.number(arg):
            sys.stdout.write( errors["type"] + arg + "\n" )
            sys.exit(1)

        result -= min_types.numberValue( arg )

def divide(args):
    if not min_types.number( args[0] ):
        sys.stdout.write( errors["type"] + arg + "\n" )
        sys.exit(1)

    result = min_types.number( args[0] )

    for arg in args[1:]:
        if not min_types.number(arg):
            sys.stdout.write( errors["type"] + arg + "\n" )
            sys.exit(1)

        result /= min_types.numberValue( arg )


def multiply(args):
    result = 1
    for arg in args:
        if not min_types.number(arg):
            sys.stdout.write( errors["type"] + arg + "\n" )
            sys.exit(1)

        result *= min_types.numberValue(arg)

functions = {
    "write":   write,
    "writeln": writeln,

    "+": plus,
    "-": minus,
    "/": divide,
    "*": multiply
}
