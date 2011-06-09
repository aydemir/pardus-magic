#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir="tea-"+get.srcVERSION()

def setup():
    shelltools.system("qmake src.pro PREFIX=/usr/bin")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/tea")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "NEWS-RU", "TODO")