#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr --disable-schemas-install \
			 --disable-desktop-update \
			 --disable-icon-update \
			 --enable-build-for-glade")

def build(): 
    autotools.make() 

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    pisitools.dodoc("AUTHORS", "COPYING", "INSTALL", "MAINTAINERS", "NEWS", "README", "THANKS")

