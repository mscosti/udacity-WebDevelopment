'''
Created on May 22, 2013

@author: Matt
'''
import logging
import time
import webapp2
from BlogPost import BlogPost
from google.appengine.api import memcache
from google.appengine.ext import db

def topPosts(update = False):    
    key = 'top'
    posts = memcache.get(key)
    current = time.time()
    tempTime = memcache.get('front_time')
    if posts is None or tempTime is None or update:
        posts = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC LIMIT 10")
        posts = list(posts)
        logging.error("DB QUERY - I JUST HIT THE DATABASE %s"%posts)
        memcache.set('front_time',current)
        memcache.set(key,posts)
    if tempTime:
        logging.error(tempTime)
        current = tempTime
    return posts,current

def permaPosts(id,update = False):
    post = memcache.get(id)
    current = time.time()
    tempTime = memcache.get('time_%s'%id)
    if post is None or tempTime is None or update:
        post = BlogPost.get_by_id(int(id))
        post = [post]
        memcache.set('time_%s'%id,current)
        memcache.set(id,post)
    if tempTime:
        current = tempTime
    return post,current

def flush():
    memcache.flush_all()
   
class FlushHandler(webapp2.RequestHandler):
    def get(self):
        flush()
        self.redirect('/blog')
    
    
    
    
    
    