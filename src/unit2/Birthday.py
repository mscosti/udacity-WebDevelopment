'''
Created on May 12, 2013

@author: Matt
'''

import webapp2

form = open('play.html', 'r').read()

class MainPage(webapp2.RequestHandler):
    
    def writeForm(self, error="", month="", day="", year=""):
        self.response.write(form % {"error":error, 
                                    "month":month, 
                                    "year":year, 
                                    "day": day})
        
    def get(self):
        self.writeForm()
        
    def post(self):
        userDay = self.request.get("day")
        userMonth = self.request.get("month")
        userYear = self.request.get("year")
        
        if validDay(userDay) and validMonth(userMonth) and validYear(userYear):
            self.redirect('/unit2/thanks!')
        else:
            self.writeForm("Sorry, that totally isn't valid!",userMonth,userDay,userYear)
            
        
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks, thats a totally valid day!")


def validDay(day):
    try:
        day = int(day)
        if (day >=1 and day <= 31):
            return True
        else:
            return False
    except ValueError:
        return False
    
def validYear(year):
    try:
        year = int(year)
        if (year >=1900 and year <= 2020):
            return True
        else:
            return False
    except ValueError:
        return False

def validMonth(month):
    month = month.capitalize()
    months = ('January',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December')
    for m in months:
        if month == m:
            return True
