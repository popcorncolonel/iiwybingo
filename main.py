import webapp2
import jinja2
import os
import random
import logging

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
        'Bonus Thursday episode',
        'Someone insults J&A in the question prompt',
]

free_ad = 'Things got real'
ad_events = [
        'Only Amir telling the ad',
        '3+ ads in 1 episode',
        'Naturebox',
        'Amir repeats the name of the company at least 3 times in a row',
        'Squarespace',
        'MeUndies',
        'New sponsor (first time on the show)',
        'J&A get free stuff from the ad company',
        'Jake mispronounces the company\'s name intentionally',
        'Promo code "Jake" vs. Promo code "Amir"',
]

game_data = {
        'theme' : (free_theme, theme_events),
        'show' : (free_show, show_events),
        'ad' : (free_ad, ad_events),
}

free_points = [free_ad, free_show, free_theme]

class MainHandler(webapp2.RequestHandler):
  def options(self):      
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'

  def getRows(self, gamemode):
        if gamemode == 'none':
            return None
        data = game_data[gamemode]
        events = data[1]
        l = random.sample(events, len(events)-1)
        rows = [] 
        for i in range(5):
            row = []
            for j in range(5):
                try:
                    if 5*i+j == 12: #if at midpoint
                        row.append(data[0])
                    else:
                        row.append(l[5*i + j])
                except IndexError:
                    pass
            rows.append(row)
        return rows

  def get(self):
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")

        gamemode = 'none'
        if self.request.path == '/theme':
            gamemode = 'theme'
        if self.request.path == '/show':
            gamemode = 'show'
        if self.request.path == '/ad':
            gamemode = 'ad'

        if gamemode == 'none':
            template = JINJA_ENVIRONMENT.get_template('default.html')
            self.response.write(template.render({}))
            return

        template = JINJA_ENVIRONMENT.get_template('index.html')

        rows = self.getRows(gamemode)
        
        template_values = {
                'rows': rows, #list of lists - assert(len(rows) == 25 and 13th one is the default)
                'free_points': free_points,
        }
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/show', MainHandler),
    ('/theme', MainHandler),
    ('/ad', MainHandler),
    ('/', MainHandler),
], debug=True)

