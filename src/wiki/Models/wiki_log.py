'''
Created on May 25, 2013

@author: Matt
'''
import wiki_page as wiki
from google.appengine.ext import db


class wikiLog(db.Model):
    page_title = db.StringProperty(required = True)
    versions = db.ListProperty(db.Key,required = True)