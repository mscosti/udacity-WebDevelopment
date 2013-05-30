'''
Created on May 24, 2013

@author: Matt
'''
import base
from wiki.Utils import dbManager,UserManager

class pageHandler(base.Handler):
    def get(self,title):
        version = self.request.get('V')
        if version:
            page = dbManager.getByVersion(title, int(version))
        else:
            page = dbManager.getByPage(title)
            
        if page:
            cookie = self.request.cookies.get("username")
            logged_in,user = UserManager.checkLogin(cookie)
            menu_items = self.render_menu_html(title,
                                               login=logged_in,
                                               user=user)
            self.render("wikiPage.html",
                        menu_items=menu_items,
                        content=page.content)
        else:
            self.redirect("/wiki/_edit%s"%str(title))