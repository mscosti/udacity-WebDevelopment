'''
Created on May 16, 2013

@author: Matt
'''
import os
import jinja2
import webapp2
import CacheHandler
import time
from BlogPost import BlogPost

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
        
class PermaPost(Handler):
    def get(self,postId):
        post,lastDBGet = CacheHandler.permaPosts(postId)
        self.render("homepage.html",posts=post,elapsed=int(time.time()-lastDBGet))
        