'''
Created on May 14, 2013

@author: Matt
'''
import webapp2
from unit2 import Birthday, rot13, signup
from unit3 import jinjaTest, AsciiChan
from blog import HomePage,NewPost,PermaLinkHandler,JSONHandler,CacheHandler
from unit4 import signup2,Login,Logout
from wiki.Page_Handlers import front,page,edit,history,login as wikiLogin,logout as wikiLogout,register

class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.write("Welcome!")
        
WIKIPAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/unit2/Birthday',Birthday.MainPage),
                                       ('/unit2/thanks!',Birthday.ThanksHandler),
                                       ('/unit2/rot13',rot13.Rot13Page),
                                       ('/unit2/signup',signup.SignupPage),
                                       ('/unit2/welcome',signup.WelcomeHandler),
                                       ('/unit3/jinjaTest',jinjaTest.MainPage),
                                       ('/unit3/asciichan',AsciiChan.MainPage),
                                       ('/blog',HomePage.HomePage),
                                       ('/blog/newpost',NewPost.NewPost),
                                       ('/blog/([0-9]+)',PermaLinkHandler.PermaPost),
                                       ('/blog/signup',signup2.SignupPage),
                                       ('/blog/login',Login.LoginHandler),
                                       ('/blog/logout',Logout.LogoutHandler),
                                       ('/blog/welcome',signup2.WelcomeHandler),
                                       ('/blog/.json',JSONHandler.JSONHandler),
                                       ('/blog/([0-9]+).json',JSONHandler.JSONHandler),
                                       ('/blog/flush',CacheHandler.FlushHandler),
                                       ('/wiki',front.FrontHandler),
                                       ('/wiki/signup',register.SignupPage),
                                       ('/wiki/login',wikiLogin.LoginHandler),
                                       ('/wiki/logout',wikiLogout.LogoutHandler),
                                       ('/wiki/_history' + WIKIPAGE_RE,history.historyHandler),
                                       ('/wiki/_edit' + WIKIPAGE_RE,edit.editHandler),
                                       ('/wiki' + WIKIPAGE_RE,page.pageHandler)], debug=True)


# app = webapp2.WSGIApplication([('/signup', Signup),
#                                ('/login', Login),
#                                ('/logout', Logout),
#                                ('/_edit' + PAGE_RE, EditPage),
#                                (PAGE_RE, WikiPage),
#                                ],
#                               debug=DEBUG)