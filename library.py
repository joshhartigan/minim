# Name:        library.py
# Author:      Josh Hartigan
# Description: Minim Scripting Language - Standard library definitions.

import sys

import min_types
import variables

errors = {
    "not_found": "*** NotFoundError: Specified identifier doesn't exist.",
    "empty_var": "*** EmptyVarError: No name or value given in declaration."
}

def write(args):
    values = []

    for arg in args:
        if min_types.string(arg):
            values.append( min_types.stringValue(arg) )
        elif arg in variables.varTable.keys():
            values.append( str(variables.varTable[arg]) )

    sys.stdout.write(" ".join(values))

def writeln(args):
    write(args)
    sys.stdout.write("\n")

functions = {
    "write":   write,
    "writeln": writeln
}
