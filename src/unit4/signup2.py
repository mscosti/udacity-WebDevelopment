'''
Created on May 20, 2013

@author: Matt
'''

import webapp2
import os
import jinja2
import secureHashing as h
from google.appengine.ext import db
from UserModel import User
from validations import verifySignup

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_or_select_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class SignupPage(Handler):
    
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
                self.redirect('/blog/welcome')
        else:
            self.renderFront(username,"","",email,validCheck.errors)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        userCookie = self.request.cookies.get('username','')
        if h.validateCookie(userCookie):
            user = userCookie.split('|')
            self.response.write("Welcome, %s!" % user[0])
        else:
            self.response.write("ERROR: 404")


