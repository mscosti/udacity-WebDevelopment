'''
Created on May 23, 2013

@author: Matt
'''
import webapp2
import base
import wiki.Utils.dbManager as dbManager
from google.appengine.ext import db
from wiki.Utils import UserManager

class FrontHandler(base.Handler):
    def get(self):
        front = dbManager.loadFront()
        cookie = self.request.cookies.get("username")
        logged_in,user = UserManager.checkLogin(cookie)
        menu_items = self.render_menu_html('/',
                                           login=logged_in,
                                           user=user)
        self.render("wikiPage.html",
                    menu_items=menu_items,
                    content=front.content,
                    time=front.edited)
    