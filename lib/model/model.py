#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
from datetime import datetime
import os
import MySQLdb

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_INI = os.path.join(FILE_DIR, "../..", "config.ini")

class Model(object):

    user = None
    passwd = None
    db = None
    charset = None
    con = None
    cur = None

    @classmethod
    def connect(self):
        if self.user is None:
            self.read_conf()
        if self.con is None:
            self.con = MySQLdb.connect(user=self.user, passwd=self.passwd, 
                                      db=self.db, charset=self.charset,
                                      use_unicode=True)
            self.cur = self.con.cursor()

    @classmethod
    def read_conf(self):
        conf = ConfigParser.SafeConfigParser()
        conf.read(CONFIG_INI)
        
        self.user = conf.get('db', 'username')
        self.passwd = conf.get('db', 'password')
        self.db = conf.get('db', 'db')
        self.charset = conf.get('db', 'charset')

    def __init__(self):
        pass

    def str_to_datetime(self, date, time):
        return datetime.strptime(date + 'T' + time + 'Z', "%Y.%m.%dT%H:%M:%SZ")
