#!/usr/bin/python

## This script, when executed, logs the temperature on a database 
## as well as time and date.

import os
from datetime import datetime
import sqlite3 as lite
import sys

# Get temperature
def readTemp():
        tempfile = open("/sys/bus/w1/devices/28-0000076bda99/w1_slave")
        tempfile_text = tempfile.read()
        tempfile.close()
        tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
        tempF = tempC*9.0/5.0+32.0
        return tempC,tempF

# Get the Date & Time from the system
def readTime():
        now = datetime.now()
        date = '%04d'%now.year +'-'+ '%02d'%now.month +'-'+ '%02d'%now.day
        time = '%02d'%now.hour +'-'+ '%02d'%now.minute +'-'+ '%02d'%now.second
        return date,time

# Function to log the actual Date, Time and Temperatures on the temperature TABLE
def logTemp():
        date, time = readTime()
        tempC, tempF = readTemp()

        con = None

        try:
                con = lite.connect('/home/pi/Developer/temperature/myTempTime.db')
                cur = con.cursor()
                cur.execute("INSERT INTO temperature VALUES(\'" + date + "\',\'" + time + "\'," + str(tempC) + "," + str(tempF) + ");")
                con.commit()
        except lite.Error as e:
                print("Error:" + e.arg[0])
                sys.exit(1)
        finally:
                if con:
                        con.close()
        
        return

# Function to initialize the Database and create the TABLE
def createDB():
        can = None
        try:
                con = lite.connect('/home/pi/Developer/temperature/myTempTime.db')
                cur = con.cursor()
                cur.execute("DROP TABLE IF EXISTS temperature")
                cur.execute("CREATE TABLE temperature(date text, time text, tempC float, tempF float)")
        except lite.Error as e:
                print("Error:" + e.arg[0])
                sys.exit(1)
        finally:
                if con:
                        con.close()
        
        return

logTemp()
