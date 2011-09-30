#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt4
from pisi.actionsapi import get


WorkDir="tea-"+get.srcVERSION()

def setup():
    qt4.configure(projectfile="src.pro", parameters="", installPrefix="/usr/bin")
    
def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "NEWS-RU", "TODO")