import ServerAPI, User, Session
server = ServerAPI.ServerAPI()

userDetails0 = User.UserInformation()
sessionDetails0 = Session.SessionInformation()
sessionDetails1 = Session.SessionInformation()
print "-------------------------------------------"
print server.Register(userDetails0, sessionDetails0)
print "[False, 'Error: No IP address']"

print "-------------------------------------------"
sessionDetails0.IP = "101.01.0.1"
print server.Register(userDetails0, sessionDetails0)
print "[False, 'Error: No username']"

print "-------------------------------------------"
userDetails0.username = "jingalls"
print server.Register(userDetails0, sessionDetails0)
print "[False, 'Error: No password']"

print "-------------------------------------------"
userDetails0.password = "password0123456789"
print server.Register(userDetails0, sessionDetails0)
print "[False, 'Error: No email']"

print "-------------------------------------------"
userDetails0.email = "jingalls@jingalls.com"
print server.Register(userDetails0, sessionDetails0)
print "[False, 'Error: No name']"

print "-------------------------------------------"
userDetails0.name = "Jack Ingalls"
print server.Register(userDetails0, sessionDetails0)[1]
print sessionDetails0.cookie
print sessionDetails0.sessionID
print sessionDetails0.username
print sessionDetails0.IP
print server.Register(userDetails0, sessionDetails0)

sessionDetails1.sessionID = 0
sessionDetails1.username = "jingalls"
sessionDetails1.cookie = sessionDetails0.cookie
print server.ProfileInfo(sessionDetails1)
print server.ProfileInfo(sessionDetails0)
print server.SignOut(sessionDetails1)
print server.SignOut(sessionDetails0)
print server.SignOut(sessionDetails0)
print server.ProfileInfo(sessionDetails0)
print server.LogIn(userDetails0, sessionDetails0)
print server.ProfileInfo(sessionDetails0)
