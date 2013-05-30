'''
Created on May 15, 2013

@author: Matt
'''
import os
import webapp2
import jinja2
import urllib2
from xml.dom import minidom
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_or_select_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    
    def renderFront(self,title="",newArt="",error="",arts=""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC LIMIT 10")
        arts = list(arts)
        points = filter(None,(art.coords for art in arts))
        imgURL = GMAPS_URL[:-1]
        if points:
            imgURL = gmaps_img(points)
        self.render("asciiChanForm.html",
                    title=title,
                    newArt=newArt,
                    error=error,
                    arts=arts,
                    imgURL=imgURL)
        
    def get(self):
        self.renderFront()
        
    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        coords = get_coords(self.request.remote_addr)
        
        if title and art:
            a = Art(title=title,art=art)
            if coords:
                a.coords = coords
            a.put()
            self.redirect("/unit3/asciichan")
        else:
            error = "Need both a title and art please!"
            self.renderFront(title,art,error,)
    
class Art(db.Model):
    title = db.StringProperty(required=True)
    art = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    coords = db.GeoPtProperty()

ipURL = "http://api.hostip.info/?ip="
def get_coords(ip):
    url = ipURL + ip
    content = None
    try:
        content = urllib2.urlopen(url).read()
    except urllib2.URLError:
        return
    xmlString = minidom.parseString(content)
    coordTag = xmlString.getElementsByTagName("gml:coordinates")
    if coordTag and coordTag[0].childNodes[0].nodeValue:
        lon, lat = coordTag[0].childNodes[0].nodeValue.split(',')
        return db.GeoPt(lat,lon)
    else:
        return  

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&"
def gmaps_img(points):
    url = GMAPS_URL
    for p in points:
        url += "markers=%s,%s&"%(p.lat,p.lon)
    return url[:-1]
    
        