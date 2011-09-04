#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# def setup

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("NEWS", "COPYING", "README")