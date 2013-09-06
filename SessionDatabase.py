# -*- coding: utf-8 -*-
"""
Created on Fri Sep 06 16:43:37 2013

@author: Jack
"""

class SessionInformation:
    def __init__(self):
        username = None
        IP = None
        cookie = None
        SessionID = None

class SessionDatabase:
    def __init__(self):
        myTable = {}
        nextSessionID = 0
    
    def AddSession(self, sessionDetails):
        pass

    def RemoveSession(self, sessionDetails):
        pass

    def ValidSession(self, sessionDetails):
        pass