#!/usr/bin/python
#
# ClamTk, copyright (C) 2004-2017 Dave M
#
# This file is part of ClamTk (http://code.google.com/p/clamtk/).
#
# ClamTk is free software; you can redistribute it and/or modify it
# under the terms of either:
#
# a) the GNU General Public License as published by the Free Software
# Foundation; either version 1, or (at your option) any later version, or
#
# b) the "Artistic License".

import os
import pipes

import locale
locale.setlocale(locale.LC_ALL, '')

import gettext
_ = lambda x: gettext.ldgettext("clamtk-gnome", x)

from gi.repository import Nautilus, GObject


class OpenTerminalExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        print("Initializing clamtk-gnome")

    def _open_scanner(self, files):
        allPaths = list ()
        for file in files:
            filename = file.get_location().get_path()
            #- file is of type nautiuls-vsf-file
            # https://github.com/GNOME/nautilus/blob/master/src/nautilus-file.h
            # which inherits from nautilus-file
            # https://github.com/GNOME/nautilus/blob/master/src/nautilus-vfs-file.h
            #- get_location returns a GFile
            # https://developer.gnome.org/gio/stable/GFile.html
            # which has the get_path function which returns the absolute path as a string
            filename = pipes.quote(filename)
            # - when switching to Python 3 we can use shlex.quote() instead
            allPaths.append (filename)
        print (' '.join(allPaths))
        os.system('clamtk %s &' % ' '.join(allPaths))

    def menu_activate_cb(self, menu, files):
        self._open_scanner(files)

    def menu_background_activate_cb(self, menu, files):
        self._open_scanner(files)

    def get_file_items(self, window, files):
        if len(files) < 1:
            return
        else:
            item = Nautilus.MenuItem(
                name='NautilusPython::openscanner',
                label=_('Scan for threats...') ,
                tip=_('Scan for threats...'),
                icon='clamtk')
            # - the tooltips are not shown any longer in Nautilus
            # (the code is kept here in case this changes again for Nautilus
            item.connect('activate', self.menu_activate_cb, files)
            return [item]


    def get_background_items(self, window, file):
        item = Nautilus.MenuItem(
            name='NautilusPython::openscanner_directory',
            label=_('Scan directory for threats...'),
            tip=_('Scan this directory for threats...'),
            icon='clamtk')
        # - the tooltips are not shown any longer in Nautilus
        # (the code is kept here in case this changes again for Nautilus
        item.connect('activate', self.menu_background_activate_cb, file)

        return [item]
