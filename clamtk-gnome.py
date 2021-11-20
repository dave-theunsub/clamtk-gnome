#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ClamTk, copyright (C) 2004-2021 Dave M, Tord Dellsén
#
# This file is part of ClamTk
# (https://gitlab.com/dave_m/clamtk/wikis/Home)
#
# ClamTk is free software; you can redistribute it and/or modify it
# under the terms of either:
#
# a) the GNU General Public License as published by the Free Software
# Foundation; either version 1, or (at your option) any later version, or
#
# b) the "Artistic License".

import locale
import subprocess

locale.setlocale(locale.LC_ALL, "")

import gettext

gettext.bindtextdomain("clamtk", "/usr/share/locale")
gettext.textdomain("clamtk")
_ = gettext.gettext

import gi

gi.require_version("Nautilus", "3.0")

from gi.repository import Nautilus
from gi.repository import GObject


class OpenTerminalExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        print("Initializing clamtk-gnome")

    def _open_scanner(self, file):
        filename = file.get_location().get_path()
        # - file is of type nautiuls-vsf-file
        # https://github.com/GNOME/nautilus/blob/master/src/nautilus-file.h
        # which inherits from nautilus-file
        # https://github.com/GNOME/nautilus/blob/master/src/nautilus-vfs-file.h
        # - get_location returns a GFile
        # https://developer.gnome.org/gio/stable/GFile.html
        # which has the get_path function which returns the absolute path as a string

        cmd = ["clamtk", filename]
        subprocess.Popen(cmd)

    def menu_activate_cb(self, menu, file):
        self._open_scanner(file)

    def menu_background_activate_cb(self, menu, file):
        self._open_scanner(file)

    def get_file_items(self, window, files):
        if len(files) != 1:
            return
        file = files[0]

        item = Nautilus.MenuItem(
            name="NautilusPython::openscanner",
            label=_("Scan for threats..."),
            tip=_("Scan for threats..."),
            icon="clamtk",
        )
        # - the tooltips are not shown any longer in Nautilus
        # (the code is kept here in case this changes again for Nautilus)
        item.connect("activate", self.menu_activate_cb, file)

        return [item]

    def get_background_items(self, window, file):
        item = Nautilus.MenuItem(
            name="NautilusPython::openscanner_directory",
            label=_("Scan directory for threats..."),
            tip=_("Scan this directory for threats..."),
            icon="clamtk",
        )
        # - the tooltips are not shown any longer in Nautilus
        # (the code is kept here in case this changes again for Nautilus
        item.connect("activate", self.menu_background_activate_cb, file)

        return [item]
