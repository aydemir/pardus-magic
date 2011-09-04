#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import fileinput
from stat import *

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    ls = os.listdir('/home')
    for it in ls:
        if os.path.isdir('/home/' + it):
            file = '/home/' + it + '/.openttd/openttd.cfg'
            if os.path.isfile(file):
                st = os.stat(file)
                for line in fileinput.input(file, inplace =1):
                    line = line.strip()
                    if re.search('^(small|medium|large)_(font|size)\s=($|\s\d+$)',  line) == None:
                        print line
                os.chown(file,  st[ST_UID],  st[ST_GID])
