'''
Created on May 16, 2013

@author: Matt
'''

import os
import webapp2
import jinja2
import BlogPost
import time
import CacheHandler
from google.appengine.api import memcache
from google.appengine.ext import db

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
        
class HomePage(Handler):
    def get(self):
        allPosts,lastDBGet = CacheHandler.topPosts()
        if lastDBGet:
            self.render("homepage.html",posts=allPosts,elapsed=int(time.time()-lastDBGet))
        else:
            self.render("homepage.html",posts=allPosts,elapsed=0)

            
