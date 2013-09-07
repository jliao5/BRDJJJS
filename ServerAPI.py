# -*- coding: utf-8 -*-
"""
Created on Fri Sep 06 16:42:05 2013

@author: Jack
"""

import Session
import User

class ServerAPI:
    def __init__(self):
        self.sessions = SessionDatabase.SessionDatabase()
        self.users = UserDatabase.UserDatabase()

    def LogIn(self, userDetails, sessionDetails):
        correctPassword = self.users.CorrectPassword(userDetails)
        if not correctPassword[0]:
            return correctPassword
        sessionDetails.username = userDetails.username
        return self.sessions.AddSession(sessionDetails)

    def ProfileInfo(self, sessionDetails):
        validation = self.sessions.ValidSession(sessionDetails)
        if not validation[0]:
            return validation
        userDetails = UserDatabase.UserInformation(
            username=sessionDetails.username
            )
        return self.users.GetUserInfo(userDetails)

    def Register(self, userDetails, sessionDetails):
        IP = sessionDetails.IP
        if IP is None:
            return [False, "Error: No IP address"]
        
        registration = self.users.AddUser(userDetails)
        if not registration[0]:
            return registration
        return LogIn(userDetails, sessionDetails)

    def SignOut(self, sessionDetails):
        return self.sessions.RemoveSession(sessionDetails)
