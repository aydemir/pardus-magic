#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="redeclipse"

#def setup():


def build():
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.doexe("src/reserver", "/usr/share/redeclipse/bin/")
    pisitools.doexe("src/reclient", "/usr/share/redeclipse/bin/")
    pisitools.dodoc("license.txt", "readme.txt")
    shelltools.copytree("data/", "%s/usr/share/redeclipse" % get.installDIR())

