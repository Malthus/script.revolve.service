# *  Script: Revolve/Helper Script

import sys

import resources.xbmclibrary as xbmclibrary
import resources.populatesubmenufromskinvariables as populatesubmenufromskinvariables
import resources.clearproperties as clearproperties
import resources.fillpropertyfromtextfile as fillpropertyfromtextfile
import resources.swapmenuoptions as swapmenuoptions
import resources.executeshellcommand as executeshellcommand
import resources.generaterandomnumber as generaterandomnumber


SCRIPTNAME = 'Revolve/Main'


function = "-"
if len(sys.argv) > 1:
    try:
        function = sys.argv[1]
         
        if function == "PopulateSubmenuFromSkinVariables":
            populatesubmenufromskinvariables.execute(sys.argv)
        elif function == "ClearProperties":
            clearproperties.execute(sys.argv)
        elif function == "FillPropertyFromTextFile":
            fillpropertyfromtextfile.execute(sys.argv)
        elif function == "SwapMenuOptions":
            swapmenuoptions.execute(sys.argv)
        elif function == "ExecuteShellCommand":
            executeshellcommand.execute(sys.argv)
        elif function == "GenerateRandomNumber":
            generaterandomnumber.execute(sys.argv)
        else:
            xbmclibrary.write_error_message(SCRIPTNAME, SCRIPTNAME + ' terminates: function ' + function + ' is unknown.')
    except BaseException as exception:
        xbmclibrary.write_error_message(SCRIPTNAME, SCRIPTNAME + ' terminates: ' + str(exception) + '.')
else:
    xbmclibrary.write_error_message(SCRIPTNAME, SCRIPTNAME + ' terminates: Missing argument(s) in call to script.')
