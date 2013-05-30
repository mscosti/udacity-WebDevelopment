'''
Created on May 24, 2013

@author: Matt
'''
import base
import time
from wiki.Utils import dbManager, UserManager

class editHandler(base.Handler):
    def get(self,title):
        page = dbManager.getByPage(title)
        content = ""
        if page:
            content = page.content
            
        cookie = self.request.cookies.get("username")
        logged_in,user = UserManager.checkLogin(cookie)
        
        if not logged_in:
            self.redirect_page(title)
            
        menu_items = self.render_menu_html(title,
                                           login=logged_in,
                                           user=user,
                                           edit=True)
        self.render('wikiEdit.html',menu_items=menu_items,title=title,content=content)
    
    def post(self,title):
        content = self.request.get('content')
        dbManager.saveEdit(title,content)
        self.redirect_page(title)