# *  Function: Revolve/swap_menu_skinsettings

import sys
import xbmc

import resources.baselibrary as baselibrary
import resources.xbmclibrary as xbmclibrary


FUNCTIONNAME = 'Revolve/swap_menu_skinsettings'
LOCKPROPERTY = '.Lock'


def get_lock_on_option(optionbase, targetwindow):
    return xbmclibrary.get_item_from_property(optionbase + LOCKPROPERTY, targetwindow)


def set_lock_on_option(optionbase, targetwindow, lockid):
    if get_lock_on_option(optionbase, targetwindow) == '':
        xbmclibrary.set_item_to_locked_property(optionbase + LOCKPROPERTY, lockid, targetwindow)
    return get_lock_on_option(optionbase, targetwindow) == lockid


def release_lock_on_option(optionbase, targetwindow):
    xbmclibrary.clear_property(optionbase + LOCKPROPERTY, targetwindow)


def check_menu_option_locks(sourcebase, targetbase, targetwindow, lockid):    
    return (get_lock_on_option(sourcebase, targetwindow) == lockid) and (get_lock_on_option(targetbase, targetwindow) == lockid)

    
def set_menu_option_locks(propertymask, targetwindow, index, otherindex, lockid):
    sourcebase = propertymask % (index)
    targetbase = propertymask % (otherindex)

    if check_menu_option_locks(sourcebase, targetbase, targetwindow, ''):
        if set_lock_on_option(sourcebase, targetwindow, lockid):
            set_lock_on_option(targetbase, targetwindow, lockid)
    
    return check_menu_option_locks(sourcebase, targetbase, targetwindow, lockid)

def release_menu_option_locks(propertymask, targetwindow, index, otherindex):
    sourcebase = propertymask % (index)
    release_lock_on_option(sourcebase, targetwindow)

    targetbase = propertymask % (otherindex)
    release_lock_on_option(targetbase, targetwindow)


def swap_menu_properties(propertymask, targetwindow, index, otherindex):
    sourcebase = propertymask % (index)
    targetbase = propertymask % (otherindex)

    xbmclibrary.swap_properties(sourcebase + '.Type', targetbase + '.Type', targetwindow)
    xbmclibrary.swap_properties(sourcebase + '.Active', targetbase + '.Active', targetwindow)
    xbmclibrary.swap_properties(sourcebase + '.Name', targetbase + '.Name', targetwindow)
    xbmclibrary.swap_properties(sourcebase + '.Subtitle', targetbase + '.Subtitle', targetwindow)
    xbmclibrary.swap_properties(sourcebase + '.BackgroundImage', targetbase + '.BackgroundImage', targetwindow)
    xbmclibrary.swap_properties(sourcebase + '.MenuTitle', targetbase + '.MenuTitle', targetwindow)
    xbmclibrary.swap_properties(sourcebase + '.SourceInfo', targetbase + '.SourceInfo', targetwindow)
    xbmclibrary.swap_properties(sourcebase + '.Window', targetbase + '.Window', targetwindow)
    xbmclibrary.swap_properties(sourcebase + '.Action', targetbase + '.Action', targetwindow)


def swap_menu_skinsettings(skinsettingmask, index, otherindex):
    sourcebase = skinsettingmask % (index)
    targetbase = skinsettingmask % (otherindex)
    
    xbmclibrary.swap_skinsettings(sourcebase + '.Type', targetbase + '.Type')
    xbmclibrary.swap_boolean_skinsettings(sourcebase + '.Active', targetbase + '.Active')
    xbmclibrary.swap_skinsettings(sourcebase + '.Name', targetbase + '.Name')
    xbmclibrary.swap_skinsettings(sourcebase + '.Subtitle', targetbase + '.Subtitle')
    xbmclibrary.swap_skinsettings(sourcebase + '.BackgroundImage', targetbase + '.BackgroundImage')
    xbmclibrary.swap_skinsettings(sourcebase + '.MenuTitle', targetbase + '.MenuTitle')
    xbmclibrary.swap_skinsettings(sourcebase + '.SourceInfo', targetbase + '.SourceInfo')
    xbmclibrary.swap_skinsettings(sourcebase + '.Window', targetbase + '.Window')
    xbmclibrary.swap_skinsettings(sourcebase + '.Action', targetbase + '.Action')

    
def execute(arguments):
    if len(arguments) > 6:
        skinsettingmask = arguments[2]
        propertymask = arguments[3]
        index = int(arguments[4])
        otherindex = int(arguments[5])
        targetwindow = arguments[6]
        lockid = 'Lock' + str(index) + str(otherindex) + str(baselibrary.get_time_in_milliseconds())

        if set_menu_option_locks(propertymask, targetwindow, index, otherindex, lockid):
            swap_menu_skinsettings(skinsettingmask, index, otherindex)
            swap_menu_properties(propertymask, targetwindow, index, otherindex)
            release_menu_option_locks(propertymask, targetwindow, index, otherindex)
    else:
        xbmclibrary.write_error_message(FUNCTIONNAME, FUNCTIONNAME + ' terminates: Missing argument(s) in call to script.')	
