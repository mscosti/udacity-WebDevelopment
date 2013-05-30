'''
Created on May 16, 2013

@author: Matt
'''
from google.appengine.ext import db

class BlogPost(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)