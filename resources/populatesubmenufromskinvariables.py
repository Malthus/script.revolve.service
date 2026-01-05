# *  Function: Revolve/PopulateSubmenuFromSkinVariables

import sys
import xbmc

import resources.baselibrary as baselibrary
import resources.xbmclibrary as xbmclibrary

FUNCTIONNAME = 'Revolve/PopulateSubmenuFromSkinVariables'
DEFAULTTARGETMASK = 'MySubmenu%02dOption'
DEFAULTTARGETWINDOW = '0'
TOTALITEMS = 20

def copy_properties(sourcemask, targetmask, targetwindow):
    for index in range (1, TOTALITEMS + 1):
        sourcebase = sourcemask % (index)
        targetbase = targetmask % (index)

        for key in baselibrary.CUSTOMOPTIONKEYS:
            if key == 'Active':
                xbmclibrary.copy_boolean_skinsetting_to_property(sourcebase + '.' + key, targetbase + '.' + key, targetwindow)
            else:
                xbmclibrary.copy_skinsetting_to_property(sourcebase + '.' + key, targetbase + '.' + key, targetwindow)

#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.Type', targetbase + '.Type', targetwindow)
#        xbmclibrary.copy_boolean_skinsetting_to_property(sourcebase + '.Active', targetbase + '.Active', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.Name', targetbase + '.Name', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.Subtitle', targetbase + '.Subtitle', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.BackgroundImage', targetbase + '.BackgroundImage', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.Window', targetbase + '.Window', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.MenuIdentifier', targetbase + '.MenuIdentifier', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.ContentPath', targetbase + '.ContentPath', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.Addon', targetbase + '.Addon', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.Executable', targetbase + '.Executable', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.Parameters', targetbase + '.Parameters', targetwindow)
#        xbmclibrary.copy_skinsetting_to_property(sourcebase + '.Action', targetbase + '.Action', targetwindow)


def execute(arguments):
    if len(arguments) > 2:
        sourcemask = arguments[2]
        targetmask = baselibrary.extract_argument(arguments, 3, DEFAULTTARGETMASK)
        targetwindow = baselibrary.extract_argument(arguments, 4, DEFAULTTARGETWINDOW)
        
        copy_properties(sourcemask, targetmask, targetwindow)
    else:
        xbmclibrary.write_error_message(FUNCTIONNAME, FUNCTIONNAME + ' terminates: Missing argument(s) in call to script.')	
