# *  Function: Revolve/ExecuteShellCommand

import os
import sys
import xbmc

import resources.baselibrary as baselibrary
import resources.xbmclibrary as xbmclibrary


FUNCTIONNAME = 'Revolve/ExecuteShellCommand'
DEFAULTTARGETWINDOW = '0'


def execute(arguments):
    if len(sys.argv) > 2:
        shellcommand = sys.argv[2]
        os.system(shellcommand)
    else:
        xbmclibrary.write_error_message(FUNCTIONNAME, FUNCTIONNAME + ' terminates: Missing argument(s) in call to script.')	
