# *  Function: Revolve/swapMenuSkinSettings

import sys
import xbmc

import xbmclibrary

FUNCTIONNAME = 'Revolve/swapMenuSkinSettings'

def swapMenuProperties(propertymask, targetwindow, index, otherindex):
    sourcebase = propertymask % (index)
    targetbase = propertymask % (otherindex)

    xbmclibrary.swapProperties(sourcebase + '.Type', targetbase + '.Type', targetwindow)
    xbmclibrary.swapProperties(sourcebase + '.Active', targetbase + '.Active', targetwindow)
    xbmclibrary.swapProperties(sourcebase + '.Name', targetbase + '.Name', targetwindow)
    xbmclibrary.swapProperties(sourcebase + '.Subtitle', targetbase + '.Subtitle', targetwindow)
    xbmclibrary.swapProperties(sourcebase + '.BackgroundImage', targetbase + '.BackgroundImage', targetwindow)
    xbmclibrary.swapProperties(sourcebase + '.MenuTitle', targetbase + '.MenuTitle', targetwindow)
    xbmclibrary.swapProperties(sourcebase + '.SourceInfo', targetbase + '.SourceInfo', targetwindow)
    xbmclibrary.swapProperties(sourcebase + '.Window', targetbase + '.Window', targetwindow)
    xbmclibrary.swapProperties(sourcebase + '.Action', targetbase + '.Action', targetwindow)

def swapMenuSkinSettings(skinsettingmask, index, otherindex):
    sourcebase = skinsettingmask % (index)
    targetbase = skinsettingmask % (otherindex)
    
    xbmclibrary.swapSkinSettings(sourcebase + '.Type', targetbase + '.Type');
    xbmclibrary.swapBooleanSkinSettings(sourcebase + '.Active', targetbase + '.Active');
    xbmclibrary.swapSkinSettings(sourcebase + '.Name', targetbase + '.Name');
    xbmclibrary.swapSkinSettings(sourcebase + '.Subtitle', targetbase + '.Subtitle');
    xbmclibrary.swapSkinSettings(sourcebase + '.BackgroundImage', targetbase + '.BackgroundImage');
    xbmclibrary.swapSkinSettings(sourcebase + '.MenuTitle', targetbase + '.MenuTitle');
    xbmclibrary.swapSkinSettings(sourcebase + '.SourceInfo', targetbase + '.SourceInfo');
    xbmclibrary.swapSkinSettings(sourcebase + '.Window', targetbase + '.Window');
    xbmclibrary.swapSkinSettings(sourcebase + '.Action', targetbase + '.Action');

def execute(arguments):
    if len(arguments) > 6:
        skinsettingmask = arguments[2]
        propertymask = arguments[3]
        index = int(arguments[4])
        otherindex = int(arguments[5])
        targetwindow = arguments[6]

        swapMenuSkinSettings(skinsettingmask, index, otherindex)
        swapMenuProperties(propertymask, targetwindow, index, otherindex)
    else:
        xbmclibrary.writeErrorMessage(FUNCTIONNAME, FUNCTIONNAME + ' terminates: Missing argument(s) in call to script.')	
