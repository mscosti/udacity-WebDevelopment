'''
Created on May 20, 2013

@author: Matt
'''
'''
Created on May 20, 2013

@author: Matt
'''
import webapp2


class LogoutHandler(webapp2.RequestHandler):
           
    def get(self):
        if self.request.cookies.get('username'):
            self.response.delete_cookie('username')
        self.redirect('/blog/signup')
    
        

            
            
            