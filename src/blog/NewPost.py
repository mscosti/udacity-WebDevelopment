'''
Created on May 16, 2013

@author: Matt
'''
'''
Created on May 15, 2013

@author: Matt
'''
import os
import webapp2
import jinja2
import logging
import CacheHandler
import time
from BlogPost import BlogPost
from google.appengine.api import memcache
from PermaLinkHandler import PermaPost

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

class NewPost(Handler):
    
    def renderFront(self,title="",content="",error=""):
        self.render("newpost.html",
                    title=title,
                    content=content,
                    error=error)
        
    def get(self):
        self.renderFront()
        
    def post(self):
        title = self.request.get("subject")
        content = self.request.get("content")
        
        if title and content:
            post = BlogPost(title=title,content=content)
            post.put()
            logging.error(post)
            if post.is_saved():
                CacheHandler.topPosts(True)
                self.redirect("/blog/%d"%post.key().id())
        else:
            error = "Need both subject and content please!"
            self.renderFront(title,content,error,)
    

    
    
        