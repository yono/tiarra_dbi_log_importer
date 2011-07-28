#!/usr/bin/env python
# -*- coding: utf-8 -*-

import model

class Channel(model.Model):
    def __init__(self, name, date, time):

        self.name = name
        self.created_on = self.str_to_datetime(date, time)
        self.updated_on = self.str_to_datetime(date, time)
        
        self.connect()
        self.id = self.get_by_name()
        if self.id is None:
            self.cur.execute("INSERT INTO channel(name, created_on, updated_on) VALUES('%s', '%s', '%s')" % (self.name.decode('utf-8'), self.created_on, self.updated_on))
            self.con.commit()
            self.id = self.get_by_name()
         
    def get_by_name(self):
        self.cur.execute("SELECT id FROM channel WHERE name = '%s'" % (self.name))
        row = self.cur.fetchone()
        if row is not None:
            return row[0]
        else:
            return None

    def get_by_id(self, id):
        self.cur.execute("SELECT name FROM channel WHERE id = %s" % (self.id))
        row = self.cur.fetchone()
        if row is not None:
            return row[0]
        else:
            return None
