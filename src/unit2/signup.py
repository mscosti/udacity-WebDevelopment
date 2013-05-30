'''
Created on May 14, 2013

@author: Matt
'''
import webapp2
import cgi
import re

form = open('signupPage.html', 'r').read()

class SignupPage(webapp2.RequestHandler):
    
    def writeForm(self,username="",password="",verify="",email="",Errors=["","","",""]):
        self.response.write(form % {"username":username,
                                    "password":password,
                                    "verify":verify,
                                    "email":email,
                                    "uError":Errors[0],
                                    "pError":Errors[1],
                                    "vError":Errors[2],
                                    "eError":Errors[3]})
    def get(self):
        self.writeForm()
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        
        validCheck = verifySignup(username,password,verify,email)
        
        if validCheck.verify():
            self.redirect('/unit2/welcome?username=%s'%username)
        else:
            username = htmlEscaping(username)
            email = htmlEscaping(email)
            self.writeForm(username,"","",email,validCheck.errors)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        user = self.request.get("username")
        self.response.write("Welcome, %s!" % user)

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

def htmlEscaping(word):
    return cgi.escape(word, quote=True)
    
    
    
       