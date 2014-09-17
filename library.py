# Name:        library.py
# Author:      Josh Hartigan
# Description: Minim Scripting Language - Standard library definitions.

import sys

import min_types

errors = {"type": "*** WrongTypeError: Incorrect type as argument."}

def write(args):
    values = []

    for arg in args:
        if not min_types.string(arg):
            sys.stdout.write( errors["type"] + "\n" )
            sys.exit(1)
        else:
            values.append( min_types.stringValue(arg) )

    sys.stdout.write(" ".join(values))

def writeln(args):
    write(args)
    sys.stdout.write("\n")

functions = {
    "write":   write,
    "writeln": writeln
}
