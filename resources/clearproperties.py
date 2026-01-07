# *  Function: Revolve/ClearProperties

import sys
import xbmc

import resources.baselibrary as baselibrary
import resources.xbmclibrary as xbmclibrary


FUNCTIONNAME = 'Revolve/ClearProperties'
DEFAULTTARGETWINDOW = '0'
DEFAULTTARGETMASK = 'List%02dOption'
TOTALITEMS = 20


def clear_properties_by_mask(targetmask, targetwindow):
    for index in range (1, TOTALITEMS + 1):
        targetbase = targetmask % (index)

        for key in baselibrary.CUSTOMOPTIONKEYS:
            xbmclibrary.clear_property(targetbase + '.' + key, targetwindow)

#        xbmclibrary.clear_property(targetbase + '.Name', targetwindow)
#        xbmclibrary.clear_property(targetbase + '.Subtitle', targetwindow)
#        xbmclibrary.clear_property(targetbase + '.Thumbnail', targetwindow)
#        xbmclibrary.clear_property(targetbase + '.BackgroundImage', targetwindow)
#        xbmclibrary.clear_property(targetbase + '.Action', targetwindow)


def execute(arguments):
    targetmask = baselibrary.extract_argument(arguments, 2, DEFAULTTARGETMASK)
    targetwindow = baselibrary.extract_argument(arguments, 3, DEFAULTTARGETWINDOW)
    
    clear_properties_by_mask(targetmask, targetwindow)
