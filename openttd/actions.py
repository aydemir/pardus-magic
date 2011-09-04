#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure('--prefix-dir=/usr \
                            --install-dir=/usr \
                            --without-allegro \
                            --with-zlib \
                            --with-sdl \
                            --with-png \
                            --with-freetype \
                            --with-fontconfig \
                            --with-icu \
                            --with-liblzo2 \
                            --without-iconv \
                            --binary-dir="bin" \
                            --data-dir="share/openttd"')

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_DIR=%s" % get.installDIR())
    pisitools.dodoc("changelog.txt", "readme.txt", "COPYING")
