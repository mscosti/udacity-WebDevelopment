'''
Created on May 25, 2013

@author: Matt
'''
import base
import time
from wiki.Models.wiki_page import wikiPage
from wiki.Utils import dbManager, UserManager

class historyHandler(base.Handler):
    def get(self,title):
        history = dbManager.getHistByPage(title)
        if history:
            self.write("i see data")
            versions = history.versions
            
        cookie = self.request.cookies.get("username")
        logged_in,user = UserManager.checkLogin(cookie)
            
        menu_items = self.render_menu_html(title,
                                           login=logged_in,
                                           user=user,
                                           history = True)
        self.render('wikiHistory.html',
                    menu_items=menu_items,
                    title=title,
                    history=list(wikiPage.get(version) for version in versions[::-1]))
                    
                    