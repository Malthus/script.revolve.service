# *  Library: XBMC/Kodi Wrapper

import sys
import xbmc


VALUESEPARATOR = ''
ITEMSEPARATOR = ' | '


# Filter Methods

def escape_value(value):
    return ('"' + value + '"') if '"' not in value else value
#    if '"' not in value:
#        value = '"' + value + '"'
#    return value

def get_numeric_value(value):
    return '' if value == '0' else value
#    if value == '0':
#        value = ''
#    return value

def get_localized_value(value):
    return xbmc.getLocalizedString(value)


# Recombination Methods    
    
#def join_single_value(result, value):
#    return result + value

def join_values(*values):
    return VALUESEPARATOR.join([value for value in values if value != ''])
#    result = ''
#    for value in values:
#        result = join_single_value(result, label)
#    return result
    
#def join_single_item(result, item):
#    if (result != '') and (item != ''):
#        result = result + join_single_value(' | ', item)
#    elif result == '':
#        result = item
#    return result
    
def join_items(*items):
    return ITEMSEPARATOR.join([item for item in items if item != ''])
#    result = ''
#    for item in items:
#        result = join_single_item(result, item)
#    return result

def add_prefix_to_item(prefix, item):
    return (prefix + item) if item != '' else item
    
def add_prefix_and_suffix_to_item(prefix, item, suffix):
    return (prefix + item + suffix) if item != '' else item
    
def replace_empty_item(item, nextitem):
    return item if item != '' else nextitem

    
# Data Read Methods    

def get_item_from_infolabel(infolabel):    
    return xbmc.getInfoLabel(infolabel)
    
def get_item_from_property(property, window):
    return get_item_from_infolabel('Window(' + window + ').Property(' + property + ')')

def get_item_from_homeproperty(property):
    return get_item_from_property(property, 'home')

#def get_numeric_item_from_homeproperty(property):
#    return get_numeric_value(get_item_from_property(property, 'home'))

def get_item_from_skinsetting(skinsetting):
    return get_item_from_infolabel('Skin.String(' + skinsetting + ')')

def get_boolean_item_from_skinsetting(skinsetting):
    item = get_item_from_infolabel('Skin.HasSetting(' + skinsetting + ')')
    if item != 'True':
        item = 'False'
    return item

def replace_empty_item_with_homeproperty(item, property):
    if item == '':
        item = get_item_from_homeproperty(property)
    return item

# Data Write Methods    

def clear_property(property, window):
    xbmc.executebuiltin('ClearProperty(' + property + ',' + window + ')')
    
def set_item_to_property(property, item, window):
    if item != '':
        xbmc.executebuiltin('SetProperty(' + property + ',' + escape_value(item) + ',' + window + ')')        
    else:
        xbmc.executebuiltin('ClearProperty(' + property + ',' + window + ')')
    
def set_item_to_locked_property(property, item, window):
    if item != '':
        xbmc.executebuiltin('SetProperty(' + property + ',' + escape_value(item) + ',' + window + ')', True)
    else:
        xbmc.executebuiltin('ClearProperty(' + property + ',' + window + ')', True)
    
def set_item_to_skinsetting(skinsetting, item):
    if item != '':
        xbmc.executebuiltin('Skin.SetString(' + skinsetting + ',' + escape_value(item) + ')')
    else:
        xbmc.executebuiltin('Skin.Reset(' + skinsetting + ')')
    
def set_boolean_item_to_skinsetting(skinsetting, item):
    if item == 'True':
        xbmc.executebuiltin('Skin.SetBool(' + skinsetting + ')')
    else:
        xbmc.executebuiltin('Skin.Reset(' + skinsetting + ')')
    
# Data Copy Methods    
    
def copy_skinsetting_to_property(skinsetting, property, window):
    item = get_item_from_skinsetting(skinsetting)
    set_item_to_property(property, item, window)

def copy_boolean_skinsetting_to_property(skinsetting, property, window):
    item = get_boolean_item_from_skinsetting(skinsetting)
    set_item_to_property(property, item, window)

def swap_properties(property, otherproperty, window):
    item = get_item_from_property(property, window)
    set_item_to_property(property, get_item_from_property(otherproperty, window), window)
    set_item_to_property(otherproperty, item, window)

def swap_skinsettings(skinsetting, otherskinsetting):
    item = get_item_from_skinsetting(skinsetting)
    set_item_to_skinsetting(skinsetting, get_item_from_skinsetting(otherskinsetting))
    set_item_to_skinsetting(otherskinsetting, item)

def swap_boolean_skinsettings(skinsetting, otherskinsetting):
    item = get_boolean_item_from_skinsetting(skinsetting)
    set_boolean_item_to_skinsetting(skinsetting, get_boolean_item_from_skinsetting(otherskinsetting))
    set_boolean_item_to_skinsetting(otherskinsetting, item)

   
# File Methods

def translate_path(filename):
    if filename.startswith('special://'):
        return xbmc.translatePath(filename)
    else:
        return filename


# Log Methods

def write_error_message(source, message):
    if isinstance(message, str):
        message = message.decode("utf-8")
    logmessage = u'%s: %s' % (source, message)
    xbmc.log(msg=logmessage.encode("utf-8"), level=xbmc.LOGNOTICE)

def write_debug_message(source, message):
    if isinstance(message, str):
        message = message.decode("utf-8")
    logmessage = u'%s: %s' % (source, message)
    xbmc.log(msg=logmessage.encode("utf-8"), level=xbmc.LOGDEBUG)
