'''
Created on May 24, 2013

@author: Matt
'''
import webapp2
import secureHashing as h

def checkLogin(cookie):
    if cookie:
        return h.validateCookie(cookie),getUserFromCookie(cookie)
    else:
        return False,''

def getUserFromCookie(cookie):
    return cookie.split('|')[0]
        