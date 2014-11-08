#!/usr/bin/env python

import sys, calendar

#Import the ZSI machinery
from ZSI import dispatch

def getMonth(year, month):
    return calendar.month(year, 3)

def getYear(year):
    return calendar.calendar(year)

print "Starting server..."
dispatch.AsServer(port=8080)
