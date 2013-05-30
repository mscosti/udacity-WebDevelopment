'''
Created on May 20, 2013

@author: Matt
'''
from google.appengine.ext import db


class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.TextProperty(required=True)
    email = db.EmailProperty()
    registered = db.DateTimeProperty(auto_now_add=True)
    
def getUser(username): 
    user = User.gql("WHERE username = :name",name=username)
    if user.get():
        return user.get()
    else: 
        return False
    
def getPassword(username):
    user = getUser(username)
    return user.password
        
def getUserName(username):
    user = getUser(username)
    return user.username  
        