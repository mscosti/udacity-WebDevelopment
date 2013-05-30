'''
Created on May 23, 2013

@author: Matt
'''
from google.appengine.ext import db
from wiki.Models import wiki_page as wiki
from wiki.Models import wiki_log as hist
import logging
from datetime import datetime

def loadFront():
    front = getByPage("/")
    if not front:
        logging.error("hit database")
        front = wiki.wikiPage(page_title = "/",
                              content = "<h1>Welcome to the Wiki!!</h1>")
        front.put()
        if front.save():
            return front
    return front

def getByPage(title):
    return db.GqlQuery("SELECT * FROM wikiPage WHERE page_title =:title ORDER BY edited DESC LIMIT 1",title=title).get()

def getHistByPage(title):
    return db.GqlQuery("SELECT * FROM wikiLog WHERE page_title =:title LIMIT 1",title=title).get()

def getByVersion(title,version):
    history = getHistByPage(title)
    key = history.versions[version-1]
    return wiki.wikiPage.get(key)

def saveEdit(title,content):
    page = getByPage(title)
    if page:
        edit = wiki.wikiPage(page_title=title,content=content)
        edit.edited = datetime.today()
        edit.put()
        if edit.save():
            addPageToLog(edit)
            return 
    else:
        page = wiki.wikiPage(page_title=title,content=content,edited = datetime.today())
        page.put()
        if page.save():
            addPageToLog(page)
            return
        
def addPageToLog(page):
    title = page.page_title
    log = getHistByPage(title)
    if log:
        logging.error("i have a log already")
        log.versions.append(page.key())
        log.put()
        if log.save():
            return
    else:
        logging.error("i do not have a log yet")
        key = page.key()
        log = hist.wikiLog(page_title=title,versions=[])
        log.versions.append(key)
        log.put()  
        if log.save():
            return
    