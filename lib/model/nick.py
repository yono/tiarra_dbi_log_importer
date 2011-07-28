#!/usr/bin/env python
# -*- coding: utf-8 -*-

import model

class Nick(model.Model):

    def __init__(self, name, date, time):

        self.name = name
        self.created_on = self.str_to_datetime(date, time)
        self.updated_on = self.str_to_datetime(date, time)
        
        self.connect()
        self.cur.execute("SELECT id FROM nick WHERE name = '%s'" % (name))

        row = self.cur.fetchone()
        if row is None:
            self.cur.execute("INSERT INTO nick(name, created_on, updated_on) VALUES('%s', '%s', '%s')" % (self.name.decode('utf-8'), self.created_on, self.updated_on))
            self.con.commit()
            self.cur.execute("SELECT id FROM nick WHERE name = '%s'" % (name))
            row = self.cur.fetchone()
         
       	self.id = row[0] 
