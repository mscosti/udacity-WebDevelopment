'''
Created on May 20, 2013

@author: Matt
'''

import webapp2
import os
import jinja2
import base
from wiki.Utils import secureHashing as h
from google.appengine.ext import db
from wiki.Models.UserModel import User
from wiki.Utils.validations import verifySignup

class SignupPage(base.Handler):
    
    def renderFront(self,username="",password="",verify="",email="",Errors=["","","",""]):
        self.render("signupPage2.html",
                    username=username,
                    password=password,
                    verify=verify,
                    email=email,
                    uError=Errors[0],
                    pError=Errors[1],
                    vError=Errors[2],
                    eError=Errors[3])
        
    def get(self):
        self.renderFront()
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        
        validCheck = verifySignup(username,password,verify,email)
        
        if validCheck.verify():
            password = h.makePasswordHash(password)
            if email:
                user = User(username=username,password=password,email=email)
            else:
                user = User(username=username,password=password)
            user.put()
            self.response.headers.add_header('Set-Cookie', 'username=%s; Path=/'%str(h.makeSecureCookie(username)))
            if user.is_saved():
                self.redirect_page('/')
        else:
            self.renderFront(username,"","",email,validCheck.errors)

# class WelcomeHandler(webapp2.RequestHandler):
#     def get(self):
#         userCookie = self.request.cookies.get('username','')
#         if h.validateCookie(userCookie):
#             user = userCookie.split('|')
#             self.response.write("Welcome, %s!" % user[0])
#         else:
#             self.response.write("ERROR: 404")


