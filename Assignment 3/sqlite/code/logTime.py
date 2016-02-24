#!/usr/bin/python

# Code to manipulate de testTime database
# Coded by Juvenal Bisneto
# On Feb 23rd, 2016

# TIPS:
# To run a expecific function of the file, run the following command on the prompt/terminal:
#	python -c "execfile('logTime.py'); logTime()"

from datetime import datetime
import sqlite3 as lite
import sys

# Get the Date & Time from the system
def readTime():
	now = datetime.now()
	xdate = '%04d'%now.year +'-'+ '%02d'%now.month  +'-'+ '%02d'%now.day
	xtime = '%02d'%now.hour +'-'+ '%02d'%now.minute +'-'+ '%02d'%now.second
	return xdate, xtime

# Function to log the actual Date & Time on the datetime TABLE
def logTime():
	xdate, xtime = readTime()
	
	con = None

	try:
		con = lite.connect('testTime.db')
		cur = con.cursor()
		cur.execute("INSERT INTO datetime VALUES(\'" + xdate + "\',\'" + xtime + "\');")
		con.commit()
	except lite.Error, e:
		print "Error %s:" % e.arg[0]
		sys.exit(1)
	finally:
		if con:
			con.close()

	return

# Function to initialize the Database and create the TABLE
def createDB():
	con = None
	try:
		con = lite.connect('testTime.db')
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS datetime")
		cur.execute("CREATE TABLE datetime(date text, time text)")
	except lite.Error, e:
		print "Error %s:" % e.arg[0]
		sys.exit(1)
	finally:
		if con:
			con.close()

	return