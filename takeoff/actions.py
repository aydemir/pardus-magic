#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    kde4.configure("-DCMAKE_BUILD_TYPE=Release \
		    -DCMAKE_CXX_FLAGS_RELEASE:STRING='-DNDEBUG' \
		    -DCMAKE_C_FLAGS_RELEASE:STRING='-DNDEBUG'", sourceDir="..")

def build():
    kde4.make()

def install():
    kde4.install()
    pisitools.dodoc("COPYRIGHT", "CHANGELOG", "COPYING", "README")

