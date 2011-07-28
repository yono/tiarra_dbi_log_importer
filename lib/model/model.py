#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import MySQLdb

class Model(object):
    
    user = "root"
    passwd = "taberu-ikura"
    db = "tiarra"
    charset = "utf8"
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
        pass

    def str_to_datetime(self, date, time):
        return datetime.strptime(date + 'T' + time + 'Z', "%Y.%m.%dT%H:%M:%SZ")
