# -*- coding: utf-8 -*-

import xbmc

if __name__ == '__main__':
	plugin = 'plugin://plugin.video.kingpin/'
	path = 'RunPlugin(%s?action=tools_contextkingpinSettings&opensettings=false)' % plugin
	xbmc.executebuiltin(path)
	# xbmc.executebuiltin('RunPlugin(%s?action=widgetRefresh)' % plugin) #now part of "tools_contextkingpinSettings" action