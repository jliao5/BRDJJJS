# -*- coding: utf-8 -*-
"""
Created on Fri Sep 06 16:43:37 2013

@author: Jack
"""

import random

hexChars = ('0', '1', '2', '3', '4', '5', '6', '7', 
            '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
lengthOfCookie = 128

class SessionInformation:
    def __init__(self):
        self.username = None
        self.IP = None
        self.cookie = None
        self.SessionID = None

class SessionDatabase:
    def __init__(self):
        self.myTable = {}
        self.nextSessionID = 0
    
    def AddSession(self, sessionDetails):
        username = sessionDetails.username
        if username is None:
            return [False, "Error: No username"]
            
        IP = sessionDetails.IP
        if IP is None:
            return [False, "Error: No IP address"]
            
        while True:
            newSessionID = self.nextSessionID
            self.nextSessionID = self.nextSessionID + 1
            if newSessionID not in self.myTable:
                break
        cookie = ''
        for i in range(lengthOfCookie):
            cookie += random.choice(hexChars)
        self.myTable[newSessionID] = {'username' : username,
                                      'IP' : IP,
                                      'cookie' : cookie}
        return [True, cookie]

    def RemoveSession(self, sessionDetails):
        pass

    def ValidSession(self, sessionDetails):
        pass
    