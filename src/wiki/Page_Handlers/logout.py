'''
Created on May 20, 2013

@author: Matt
'''
'''
Created on May 20, 2013

@author: Matt
'''
import base


class LogoutHandler(base.Handler):
           
    def get(self):
        if self.request.cookies.get('username'):
            self.response.delete_cookie('username')
        self.redirect_page('/')
    
        

            
            
            