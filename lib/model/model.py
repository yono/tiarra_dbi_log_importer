#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
from datetime import datetime
import MySQLdb

CONFIG_INI = "../../config.ini"

class Model(object):

    user = None
    passwd = None
    db = None
    charset = None
    con = None
    cur = None

    @classmethod
    def connect(self):
        if self.con is None:
            self.con = MySQLdb.connect(user=self.user, passwd=self.passwd, 
                                      db=self.db, charset=self.charset,
                                      use_unicode=True)
            self.cur = self.con.cursor()

    def __init__(self):
        if user is None:
            conf = ConfigParser.SafeConfigParser()
            conf.read(CONFIG_INI)
            
            self.user = conf.get('db', 'username')
            self.passwd = conf.get('db', 'password')
            self.db = conf.get('db', 'db')
            self.charset = conf.get('db', 'charset')

    def str_to_datetime(self, date, time):
        return datetime.strptime(date + 'T' + time + 'Z', "%Y.%m.%dT%H:%M:%SZ")
