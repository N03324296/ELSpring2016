#!/usr/bin/python
# -*- coding: utf-8 -*-



#####https://docs.python.org/2/library/sqlite3.html###########

import sqlite3 as mydb
import sys

con = mydb.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data

