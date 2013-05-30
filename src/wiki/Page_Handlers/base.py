'''
Created on May 23, 2013

@author: Matt
'''

import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = False)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_or_select_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
    def redirect_page(self,title):
        if title =="/":
            self.redirect("/wiki")
        else:
            self.redirect("/wiki%s"%title)
            
    def render_menu_html(self,title,**params):
        
        if not params.get('login') and params.get('history'):
            menu_items= '''
                        <a class="history" href="/wiki%(title)s">view</a>
                        
                        <a class="login" href="/wiki/login">login</a>| 
                        <a class="register" href="/wiki/signup">register</a>
                        '''%{'title':title}
        elif not params.get('login'):
            menu_items= '''
                        <a class="history" href="/wiki/_history%(title)s">history</a>
                        
                        <a class="login" href="/wiki/login">login</a>| 
                        <a class="register" href="/wiki/signup">register</a>
                        '''%{'title':title}
        elif params.get('edit'):
            menu_items= '''
                        <a class="history" href="/wiki/_history%(title)s">history</a>
                        
                         %(user)s
                        <a class="logout" href="/wiki/logout">(logout)</a>
                        '''%{'title':title,'user':params.get('user')}
        elif params.get('history'):
            menu_items= '''
                        <a class="history" href="/wiki/_edit%(title)s">edit</a>|
                        <a class="view" href="/wiki%(title)s">view
                        
                         %(user)s
                        <a class="logout" href="/wiki/logout">(logout)</a>
                        '''%{'title':title,'user':params.get('user')}
        else:
            menu_items= '''
                        <a class="edit" href="/wiki/_edit%(title)s">edit</a>|
                        <a class="history" href="/wiki/_history%(title)s">history</a>
                        
                        %(user)s
                        <a class="logout" href="/wiki/logout">(logout)</a>
                        '''%{'title':title,'user':params.get('user')}
        return menu_items