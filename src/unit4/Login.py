'''
Created on May 20, 2013

@author: Matt
'''
import webapp2
import os
import jinja2
import secureHashing as h
import validations

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

class LoginHandler(Handler):
    def renderFront(self,loginError=""):
        self.render('loginPage.html',loginError = loginError)
        
    def get(self):
        self.renderFront()
    
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        
        if validations.validateLogin(username,password):
            self.response.headers.add_header('Set-Cookie', 'username=%s; Path=/'%str(h.makeSecureCookie(username)))
            self.redirect('/blog/welcome')
        else:
            self.renderFront("Invalid Username or Password")
        

            
            
            