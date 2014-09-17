# Name:        min_types.py
# Author:      Josh Hartigan
# Description: Minim Scripting Language - Definitions of types.

import re

# determine if x is a string type
def string(x):
    return x[0] == "\"" and x[ len(x) - 1 ] == "\""
def stringValue(x):
    return x.replace("\"","")
