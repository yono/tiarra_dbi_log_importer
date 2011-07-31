#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import re
import sys
from lib.model import nick, channel, log

def import_file(filename, parent):
    _nick = {}

    infile = open(filename).read().splitlines()

    date = os.path.basename(filename).replace('.txt', '')

    regex_hatugen = re.compile(r'^[(|)|<|>|].*:(?P<name>\w+)[(|)|<|>|]$')

    _channel = None

    for line in infile:
        data = line.split(' ')
        time = data.pop(0)
        if (_channel is None):
            _channel = channel.Channel(os.path.basename(parent), date, time)
        datatype = data.pop(0)
        if regex_hatugen.search(datatype):
            name = regex_hatugen.search(datatype).group('name')
            _nick[name] = nick.Nick(name, date, time)
            _log = log.Log(' '.join(data), date, time, _nick[name], _channel)

if len(sys.argv) < 2:
    print "Usage: %s /locate/to/tiarra/log" % (sys.argv[0])
    quit()

for (root, dirs, files) in os.walk(sys.argv[1]):
    for _file in files:
        print root, _file 
        import_file(os.path.join(root, _file), root)  
