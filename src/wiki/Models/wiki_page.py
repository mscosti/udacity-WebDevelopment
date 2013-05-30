'''
Created on May 23, 2013

@author: Matt
'''
from google.appengine.ext import db
from wiki_log import wikiLog as log

class wikiPage(db.Model):
    page_title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    edited = db.DateTimeProperty()
    