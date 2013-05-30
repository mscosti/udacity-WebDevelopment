'''
Created on May 20, 2013

@author: Matt
'''
import base
from wiki.Utils import secureHashing as h
from wiki.Utils import validations

class LoginHandler(base.Handler):
    def renderFront(self,loginError=""):
        self.render('loginPage.html',loginError = loginError)
        
    def get(self):
        self.renderFront()
    
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        
        if validations.validateLogin(username,password):
            self.response.headers.add_header('Set-Cookie', 'username=%s; Path=/'%str(h.makeSecureCookie(username)))
            self.redirect_page('/')
        else:
            self.renderFront("Invalid Username or Password")
        

            
            
            