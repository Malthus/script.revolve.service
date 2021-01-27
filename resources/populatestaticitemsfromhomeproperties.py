# *  Function: Revolve/PopulateStaticItemsFromHomeProperties

import sys
import xbmc

import resources.baselibrary as baselibrary
import resources.xbmclibrary as xbmclibrary


FUNCTIONNAME = 'Revolve/PopulateStaticItemsFromHomeProperties'
DEFAULTTARGETWINDOW = '0'
DEFAULTTARGETMASK = 'MyItems%02dOption'
TOTALITEMS = 20


def create_generic_name(sourcebase):
    return xbmclibrary.replace_empty_item_with_homeproperty(xbmclibrary.get_item_from_homeproperty(sourcebase + '.Title'), sourcebase + '.EpisodeTitle')


def create_song_name(sourcebase):
    return xbmclibrary.get_item_from_homeproperty(sourcebase + '.Artist') + ' - ' + xbmclibrary.get_item_from_homeproperty(sourcebase + '.Title')


def create_favourite_name(sourcebase):
    return xbmclibrary.get_item_from_homeproperty(sourcebase + '.name')


def create_generic_subtitle(sourcebase):
    return xbmclibrary.join_items(
        xbmclibrary.get_item_from_homeproperty(sourcebase + '.ShowTitle'),
        xbmclibrary.get_item_from_homeproperty(sourcebase + '.TVShowTitle'),
        xbmclibrary.get_item_from_homeproperty(sourcebase + '.Studio'),
        xbmclibrary.get_item_from_homeproperty(sourcebase + '.Artist'),
        xbmclibrary.get_numeric_value(xbmclibrary.get_item_from_homeproperty(sourcebase + '.Year')),
        xbmclibrary.get_numeric_value(xbmclibrary.get_item_from_homeproperty(sourcebase + '.Version')))


def create_episode_subtitle(sourcebase):
    seasonNumber = xbmclibrary.replace_empty_item_with_homeproperty(xbmclibrary.get_item_from_homeproperty(sourcebase + '.Season'), sourcebase + '.EpisodeSeason')
    episodeNumber = xbmclibrary.replace_empty_item_with_homeproperty(xbmclibrary.get_item_from_homeproperty(sourcebase + '.Episode'), sourcebase + '.EpisodeNumber')
    
    return xbmclibrary.join_items(
        xbmclibrary.get_item_from_homeproperty(sourcebase + '.ShowTitle'),
        xbmclibrary.get_item_from_homeproperty(sourcebase + '.TVShowTitle'),
        xbmclibrary.add_prefix_to_item(xbmclibrary.get_localized_value(20373) + ' ', xbmclibrary.get_numeric_value(seasonNumber)),
        xbmclibrary.add_prefix_to_item(xbmclibrary.get_localized_value(20359) + ' ', xbmclibrary.get_numeric_value(episodeNumber)))


def create_song_subtitle(sourcebase):
    return xbmclibrary.join_items(
        xbmclibrary.get_item_from_homeproperty(sourcebase + '.Album'),
        xbmclibrary.get_numeric_value(xbmclibrary.get_item_from_homeproperty(sourcebase + '.Year')))


def create_favourite_subtitle(sourcebase):
    return ''


def create_generic_tumbnail(sourcebase):
    result = xbmclibrary.get_item_from_homeproperty(sourcebase + '.Art(poster)')
    result = xbmclibrary.replace_empty_item_with_homeproperty(result, sourcebase + '.thumb')
    result = xbmclibrary.replace_empty_item_with_homeproperty(result, sourcebase + '.Thumb')
    result = xbmclibrary.replace_empty_item_with_homeproperty(result, sourcebase + '.Icon')
    return result


def create_generic_backgroundimage(sourcebase):
    result = xbmclibrary.get_item_from_homeproperty(sourcebase + '.Art(Fanart)')
    result = xbmclibrary.replace_empty_item_with_homeproperty(result, sourcebase + '.Property(Fanart_image)')
    result = xbmclibrary.replace_empty_item_with_homeproperty(result, sourcebase + '.Fanart')
    return result


def create_favourite_backgroundimage(sourcebase):
    return ''


def create_generic_action(sourcebase):
    result = xbmclibrary.get_item_from_homeproperty(sourcebase + '.Play')
    if result == '':
        result = xbmclibrary.get_item_from_homeproperty(sourcebase + '.LibraryPath')
        if 'videodb' in result.lower():
            result = xbmclibrary.add_prefix_and_suffix_to_item('ActivateWindow(videos,', result, ',return)')
        if 'musicdb' in result.lower():
            result = xbmclibrary.add_prefix_and_suffix_to_item('ActivateWindow(music,', result, ',return)')
    if result == '':
        result = xbmclibrary.add_prefix_and_suffix_to_item('PlayMedia("', xbmclibrary.get_item_from_homeproperty(sourcebase + '.Path'), '")')
    return result


def create_favourite_action(sourcebase):
    return baselibrary.escape_path(xbmclibrary.get_item_from_homeproperty(sourcebase + '.path'))


def determine_name_method(sourcemask):
    result = create_generic_name    
    if 'song' in sourcemask.lower():
        result = create_song_name
    if 'favourite' in sourcemask.lower():
        result = create_favourite_name
    return result


def determine_subtitle_method(sourcemask):
    result = create_generic_subtitle
    if 'episode' in sourcemask.lower():
        result = create_episode_subtitle
    if 'song' in sourcemask.lower():
        result = create_song_subtitle
    if 'favourite' in sourcemask.lower():
        result = create_favourite_subtitle
    return result

    
def determine_thumbnail_method(sourcemask):
    return create_generic_tumbnail

    
def determine_backgroundimage_method(sourcemask):
    result = create_generic_backgroundimage
    if 'favourite' in sourcemask.lower():
        result = create_favourite_backgroundimage
    return result

    
def determine_action_method(sourcemask):
    result = create_generic_action
    if 'favourite' in sourcemask.lower():
        result = create_favourite_action
    return result

    
def copy_properties(sourcemask, targetmask, targetwindow):
    namemethod = determine_name_method(sourcemask)
    subtitlemethod = determine_subtitle_method(sourcemask)
    thumbnailmethod = determine_thumbnail_method(sourcemask)
    backgroundImagemethod = determine_backgroundimage_method(sourcemask)
    actionmethod = determine_action_method(sourcemask)

    for index in range (1, TOTALITEMS + 1):
        sourcebase = sourcemask % (index)
        targetbase = targetmask % (index)

        xbmclibrary.set_item_to_property(targetbase + '.Name', namemethod(sourcebase), targetwindow)
        xbmclibrary.set_item_to_property(targetbase + '.Subtitle', subtitlemethod(sourcebase), targetwindow)
        xbmclibrary.set_item_to_property(targetbase + '.Thumbnail', thumbnailmethod(sourcebase), targetwindow)
        xbmclibrary.set_item_to_property(targetbase + '.BackgroundImage', backgroundImagemethod(sourcebase), targetwindow)
        xbmclibrary.set_item_to_property(targetbase + '.Action', actionmethod(sourcebase), targetwindow)


def execute(arguments):        
    if len(arguments) > 2:
        sourcemask = arguments[2]
        targetmask = baselibrary.extract_argument(arguments, 3, DEFAULTTARGETMASK)
        targetwindow = baselibrary.extract_argument(arguments, 4, DEFAULTTARGETWINDOW)

        copy_properties(sourcemask, targetmask, targetwindow)
    else:
        xbmclibrary.write_error_message(FUNCTIONNAME, FUNCTIONNAME + ' terminates: Missing argument(s) in call to script.')	
