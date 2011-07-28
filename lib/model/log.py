#!/usr/bin/env python
# -*- coding: utf-8 -*-

import model
import MySQLdb

class Log(model.Model):

    def __init__(self, log, date, time, nick, channel):

        self.log = log
        self.created_on = self.str_to_datetime(date, time)
        self.updated_on = self.str_to_datetime(date, time)
        self.nick_id = nick.id
        self.channel_id = channel.id

        self.connect()
        
        self.cur.execute("INSERT INTO log(log, created_on, updated_on, channel_id, nick_id, is_privmsg) VALUES('%s', '%s', '%s', %d, %d, 1)" % (MySQLdb.escape_string(self.log.decode('utf-8')), self.created_on, self.updated_on, self.channel_id, self.nick_id))
        self.con.commit()
