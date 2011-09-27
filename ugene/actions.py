#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    if get.ARCH() == "x86_64":
        qt4.configure(projectfile='ugene.pro', parameters='CONFIG+=x64 -r', installPrefix='/usr')
    if get.ARCH() == "i686":
        qt4.configure(projectfile='ugene.pro', parameters='-r', installPrefix='/usr')
    
def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.dodoc("COPYRIGHT", "LICENSE", "data/license")
