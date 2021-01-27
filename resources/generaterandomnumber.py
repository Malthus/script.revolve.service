# *  Function: Revolve/GenerateRandomNumber

import random
import sys
import xbmc

import resources.baselibrary as baselibrary
import resources.xbmclibrary as xbmclibrary


FUNCTIONNAME = 'Revolve/GenerateRandomNumber'
DEFAULTTARGETWINDOW = '0'


def execute(arguments):
    if len(sys.argv) > 4:
        minimumvalue = sys.argv[2]
        maximumvalue = sys.argv[3]
        targetproperty = sys.argv[4]
        targetwindow = baselibrary.extract_argument(arguments, 5, DEFAULTTARGETWINDOW)
        
        randomvalue = randint(minimumvalue, maximumvalue)
        xbmclibrary.set_item_to_property(targetproperty, randomvalue, targetwindow)
    else:
        xbmclibrary.write_error_message(FUNCTIONNAME, FUNCTIONNAME + ' terminates: Missing argument(s) in call to script.')	
