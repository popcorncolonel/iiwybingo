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
        'J&A forget to mention the artist',
        'Doesn\'t rhyme',
        'Heavily borrows from Jake\'s Episode 1 theme',
        '"Beast in that regard"',
        'Uses J&A\'s voices as musical instruments',
        ]

free_show = 'Relationship question'
show_events = [
        'Live podcast',
        'Guest Episode',
        'Douchebag guy',
        'They tell someone to break up',
        'Jake approves of Amir\'s intro',
        '"Momma turn down the podcast"',
        'Something is coy',
        'Someone rhymes jokingly',
        'Jake shows appreciation for his dad\'s money',
        'Amir tries to divert attention from his middle name',
        'Jake professes his love for Amir, which is not returned',
        'Someone is "hard" or "jerking off right now"',
        'The advice Jake gives makes it sound like he\'s gotten laid in this same situation before',
        'Amir gives math advice',
        'Amir tries to turn the question into tips for him getting laid, personally',
        'Jake gives up mid-way through answering a question',
        'The guest gets put on blast or puts J&A on blast',
        'Jake gets depressed by the question',
        'The episode is hosted by Josh, Vance, or The Pinch',
        'Amir adds "-smith" to the end of an activity/occupation',
        'Tinder comes up',
        'Someone insults J&A in the question prompt',
]

free_ad = 'Things got real'
ad_events = [
        'Only Amir telling the ad',
        '3+ ads in 1 episode',
        'Promo code "Jake" vs. Promo code "Amir"',
]

free_points = [free_ad, free_show, free_theme]

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
                'rows': rows, #list of lists - assert(len(rows) == 25 and 13th one is the default)
                'free_points': free_points,
        }
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
