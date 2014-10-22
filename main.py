import webapp2
import jinja2
import os
import random

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

free_theme = 'Mentions Judaism'
theme_events = [
        'Written by Sick/sea',
        'Mentions Starbucks',
        'Says "If I Were You" at least 5 times',
        '"#Dope"',
        'Rhymes "If I Were You" with "What I\'d Do"',
        'Really good voice',
        'Really bad voice',
        'J&A insult it ironically',
        'Less than 15 seconds',
        'Stony\'s Version',
        'Rhymes "If I Were You" with "Yo Do You"',
        '"Seize the Cheese"',
        'Parody of a popular song',
        'Parody of a sitcom\'s theme song',
        'White guy rapping',
        'Mentions Kobe Bryant in the background',
        ]

free_show = 'Relationship question'
show_events = [
        'Live podcast',
        'Guest Episode',
        'Douchebag guy',
]

free_ad = 'Things got real'
ad_events = [
        'Only Amir',
        'Promo code "Jake" vs. Promo code "Amir"',
]

class MainHandler(webapp2.RequestHandler):
  def options(self):      
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'

  def themeGetRows(self):
        l = random.sample(theme_events, len(theme_events)-1)
        rows = [] 
        for i in range(5):
            row = []
            for j in range(5):
                try:
                    if 5*i+j == 12: #if at midpoint
                        row.append(free_theme)
                    else:
                        row.append(l[5*i + j])
                except IndexError:
                    pass
            rows.append(row)
        return rows

  def get(self):
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        template = JINJA_ENVIRONMENT.get_template('index.html')

        rows = self.themeGetRows()
        
        template_values = {
                'rows': rows #list of lists - assert(len(rows) == 25 and 13th one is the default)
        }
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
