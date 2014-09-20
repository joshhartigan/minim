# Name:        min_types.py
# Author:      Josh Hartigan
# Description: Minim Scripting Language - Definitions of types.

import re

# Value types
def string(x):
    return x[0] == "\"" and x[ len(x) - 1 ] == "\""
def stringValue(x):
    return x.replace("\"","")

def boolean(x):
    return x == "true" or x == "false"
def booleanValue(x):
    return True if x == "true" else False

def number(x):
    expr = re.compile("^\d+(\.\d+)?$")
    return expr.match(x)
def numberValue(x):
    return x

# Expression types
def call(x):
    return x[0] == "(" and x[ len(x) - 2 ] == ")"

def declaration(x):
    return x[:3] == "var"
