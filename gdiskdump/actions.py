#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir="gdiskdump"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.dodoc("COPYING", "AUTHORS")
    shelltools.chmod("%s/usr/share/gdiskdump/media/*.svg" % get.installDIR(), 0644)
