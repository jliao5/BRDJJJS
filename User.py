# -*- coding: utf-8 -*-
"""
Created on Fri Sep 06 16:43:37 2013

@author: Jack
"""

import random

startingNumberOfPoints = 100

class UserInformation:
    def __init__(self, username=None, password=None, email=None, name=None,
                 points=startingNumberOfPoints):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.points = points

class UserDatabase:
    def __init__(self):
        self.myTable = {}
    
    def AddUser(self, userDetails):
        username = userDetails.username
        password = userDetails.password
        email = userDetails.email
        name = userDetails.name
        
        if username is None:
            return [False, "Error: No username"]
        if username in self.myTable:
            return [False, "Error: Username already exists"]
        if password is None:
            return [False, "Error: No password"]
        if email is None:
            return [False, "Error: No email"]
        if name is None:
            return [False, "Error: No name"]
            
        self.myTable[username] = {'password' : password,
                                  'email' : email,
                                  'name' : name,
                                  'points' : startingNumberOfPoints}
        userDetails.points = startingNumberOfPoints
        return [True, userDetails]

    def RemoveUser(self, userDetails):
        correctPassword = self.CorrectPassword(userDetails)
        userInfo = self.GetUserInfo(userDetails)
        
        if not userInfo[0]:
            return userInfo
        elif not correctPassword:
            return [False, "Error: Invalid password"]
        
        self.myTable.pop(userInfo.userName)
        userInfo.password = None
        return [True, userInfo]

    def CorrectPassword(self, userDetails):
        username = userDetails.username
        password = userDetails.password

        userInfo = self.GetUserInfo(userDetails)
        if not userInfo[0]:
            return [False, "Invalid username"]
        if not (self.myTable[username]['password'] is password):
            return [False, "Wrong password"]
        return [True, "Correct password"]

    def GetUserInfo(self, userDetails):
        username = userDetails.username
        
        if username not in self.myTable:
            return [False, "Error: Invalid username"]

        userDetails.email = self.myTable[username]['email']
        userDetails.name = self.myTable[username]['name']
        userDetails.points = self.myTable[username]['points']
        return [True, userDetails]
    
