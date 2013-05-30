'''
Created on May 20, 2013

@author: Matt
'''
import re
from wiki.Models import UserModel as Users
from secureHashing import validatePassword

class verifySignup:
    
    def __init__(self,username,password,verify,email):
        self.USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        self.PASS_RE = re.compile(r"^.{3,20}$")
        self.EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        
        self.u = username
        self.p = password
        self.v = verify
        self.e = email
          
        self.valid = False
        self.errors = ["","","",""]
        self.nameError = ""
        self.passError = ""
        self.matchError = ""
        self.emailError = ""
          
    def verify(self):
        u = self.validUsername()
        p = self.validatePassword()
        e = self.validEmail()
        if (u and p and e):
            return True
        else: 
            return False
    
    def validUsername(self):
        if self.USER_RE.match(self.u):
            if Users.getUser(self.u):
                self.errors[0] = "that usernmae already exists"
                return False
            self.errors[0] = ""
            return True
        else:
            self.errors[0] = "That is not a valid username"
            return False
    
    def validatePassword(self):
        if (self.p != self.v):
            self.errors[2] = "Password does not match"
            return False
        elif (not self.PASS_RE.match(self.p) or 
              not self.PASS_RE.match(self.v)):
            self.errors[1] = "that is not a valid password"
            return False
        else:
            self.errors[1] = ""
            self.errors[2] = ""
            return True
    
    def validEmail(self):
        if (self.EMAIL_RE.match(self.e)) or self.e == "":
            self.errors[3] = ""
            return True
        else:
            self.errors[3] = "That is not a valid email"
            return False

        
def validateLogin(username,password):
    if (Users.getUser(username) and
        validatePassword(password,Users.getPassword(username))):
        return True
    else:
        return False
        
    
        
        