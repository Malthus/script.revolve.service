# *  Library: Basic Functions

import sys
import xbmc

# Methods

def extractArgument(arguments, index, defaultvalue):
    if len(arguments) > index:
        value = arguments[index]
    else:
        value = defaultvalue
    return value
