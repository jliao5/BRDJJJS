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
        self.sessionID = None

class SessionDatabase:
    def __init__(self):
        self.myTable = {}
        self.nextSessionID = 0
    
    def AddSession(self, sessionDetails):
        username = sessionDetails.username
        IP = sessionDetails.IP
        
        if username is None:
            return [False, "Error: No username"]
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
        sessionDetails.cookie = cookie
        sessionDetails.sessionID = newSessionID
        return [True, sessionDetails]

    def RemoveSession(self, sessionDetails):
        validation = self.ValidSession(sessionDetails)
        
        if validation[0]:
            username = self.myTable.pop(sessionDetails.sessionID
                                        )['username']
            validation[1] = "Logged out " + username
        return validation

    def ValidSession(self, sessionDetails):
        sessionID = sessionDetails.sessionID
        username = sessionDetails.username
        IP = sessionDetails.IP
        cookie = sessionDetails.cookie
        
        if sessionID not in self.myTable:
            return [False, "Error: Wrong sessionID"]
        if self.myTable[sessionID]['username'] is not username:
            return [False, "Error: Wrong username"]
        if self.myTable[sessionID]['IP'] is not IP:
            return [False, "Error: Wrong IP address"]
        if self.myTable[sessionID]['cookie'] is not cookie:
            return [False, "Error: Wrong cookie"]

        return [True, "Valid Session"]
    
