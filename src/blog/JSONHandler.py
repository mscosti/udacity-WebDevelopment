'''
Created on May 21, 2013

@author: Matt
'''
import webapp2
import json
from BlogPost import BlogPost
from google.appengine.ext import db


class JSONHandler(webapp2.RequestHandler):
    
    def get(self,permaID=""):
        self.response.headers["Content-Type"] = "application/json; charset=UTF-8"
        path = self.request.path
        
        if path == '/blog/.json':
            frontPosts = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC LIMIT 10")
            j = self.toJSON(frontPosts)
            self.response.write(j)
        elif permaID:
            permaPost = BlogPost.get_by_id(int(permaID))
            j = self.toJSON([permaPost])
            self.response.write(j)
       
    def toJSON(self,posts):
      
        postList =[]
        for BlogPost in posts:
            postDict = {"content":BlogPost.content,
                        "title":BlogPost.title}
            postList.append(postDict)
        return json.dumps(postList)
            
            
            