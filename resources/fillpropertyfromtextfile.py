# *  Function: Revolve/FillPropertyFromTextFile

import sys
import xbmc

import resources.baselibrary as baselibrary
import resources.xbmclibrary as xbmclibrary


FUNCTIONNAME = 'Revolve/FillPropertyFromTextFile'
DEFAULTTARGETPROPERTY = 'TextFileContent'
DEFAULTTARGETWINDOW = '0'
SPECIALFILE = 'special://'


def load_property_from_textfile(filename, targetproperty, targetwindow):
    try:
        with open(xbmclibrary.translate_path(filename)) as file:
            value = file.read()
        xbmclibrary.set_item_to_property(targetproperty, value, targetwindow)
    except IOError:
        xbmclibrary.write_error_message(FUNCTIONNAME, FUNCTIONNAME + ' terminates: Error while reading file ' + filename)


def execute(arguments):
    if len(arguments) > 2:
        filename = arguments[2]
        targetproperty = baselibrary.extract_argument(arguments, 3, DEFAULTTARGETPROPERTY)
        targetwindow = baselibrary.extract_argument(arguments, 4, DEFAULTTARGETWINDOW)

        load_property_from_textfile(filename, targetproperty, targetwindow)
    else:
        xbmclibrary.write_error_message(FUNCTIONNAME, FUNCTIONNAME + ' terminates: Missing filename in call to script.')	
