'''
Created on May 12, 2013

@author: Matt
'''

import webapp2
import cgi

form = open('rot13Form.html', 'r').read()

class Rot13Page(webapp2.RequestHandler):
    
    def get(self):
        self.response.write(form%{"text":""})
        
    def post(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        userText = self.request.get("text")
        encoded = Rot13(userText)
        self.response.write(form%{"text":encoded})
        
def Rot13(encoded):
    rot13 = ""
    mappings = {"A":"N","N":"A",
                "B":"O","O":"B",
                "C":"P","P":"C",
                "D":"Q","Q":"D",
                "E":"R","R":"E",
                "F":"S","S":"F",
                "G":"T","T":"G",
                "H":"U","U":"H",
                "I":"V","V":"I",
                "J":"W","W":"J",
                "K":"X","X":"K",
                "L":"Y","Y":"L",
                "M":"Z","Z":"M",
                
                "a":"n","n":"a",
                "b":"o","o":"b",
                "c":"p","p":"c",
                "d":"q","q":"d",
                "e":"r","r":"e",
                "f":"s","s":"f",
                "g":"t","t":"g",
                "h":"u","u":"h",
                "i":"v","v":"i",
                "j":"w","w":"j",
                "k":"x","x":"k",
                "l":"y","y":"l",
                "m":"z","z":"m",
                }
    for i in range(len(encoded)):
        char = encoded[i]
        if char in mappings:
            rot13 = rot13 +mappings[char]
        else:
            rot13 = rot13 + char
    return htmlEscaping(rot13)
 
def htmlEscaping(word):
    return cgi.escape(word, quote=True)
    
#application = webapp2.WSGIApplication([('/', MainPage)], debug=True)
