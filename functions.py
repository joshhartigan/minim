# Name:        functions.py
# Author:      Josh Hartigan
# Description: Minim Scripting Language - Function logic and function calling
#                                         logic.

import library

def processCaller(caller):
    caller = caller.replace("(","").replace(")","")

    functionName = caller.split()[0]
    arguments = caller.split()[1:]

    if functionName in library.functions:
        library.functions[functionName](arguments)

