'''
Created on May 20, 2013

@author: Matt
'''
import hashlib
import random
import string

def makeSalt():
    return ''.join(random.choice(string.letters) for x in xrange(5))  

def makePasswordHash(plainText,salt=""):
    if not salt:
        salt = makeSalt()
    h = hashlib.sha256(plainText + salt).hexdigest()
    return '%s,%s' % (h, salt)
    
def validatePassword(plainText, h):
    salt = h.split(',')[1]
    if (makePasswordHash(plainText,salt) == h):
        return True
    else:
        return

def hashString(s):
    return hashlib.md5(s).hexdigest()

def makeSecureCookie(s):
    return s + "|%s"%hashString(s)

def validateCookie(s):
    return (s == makeSecureCookie(s.split('|')[0]))