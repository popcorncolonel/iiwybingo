#Online bingo fangame for the podcast If I Were You
#http://ifiwereyoushow.com
#http://seizethecheese.com
#TODO: Mobile oh god

import webapp2
import jinja2
import os
import random
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

free_theme = 'Calls J&A Jews'
theme_events = [
        'Written by Sick/sea',
        'Mentions Starbucks',
        'Repeats "If I Were You" at least 5 times',
        '"#Dope"',
        'Rhymes "If I Were You" with "What I\'d Do"',
        'Really good voice',
        'Really bad voice',
        'J&A insult it ironically',
        'Less than 15 seconds',
        'Stony\'s Version',
        'Rhymes "If I Were You" with "Yo Do You"',
        '"Rock and a hard place"',
        '"Seize the Cheese"',
        'Really obscure podcast reference',
        'Parody of a popular song',
        'Shoehorns too many syllables into a line',
        'Parody of a sitcom\'s theme song',
        'White guy rapping',
        'Todah',
        'Catchy tune',
        'So much autotude it\'s incomprehensible',
        '"Sticky situation"',
        '"The show starts nowwwww..."',
        'J&A forget to mention the artist',
        'Doesn\'t rhyme',
        'Heavily borrows from Jake\'s Episode 1 theme',
        '"Beast in that regard"',
        'Uses samples from the podcast as musical instruments',
        ]

free_show = 'Relationship question'
show_events = [
        'Amir says "Mercy"',
        'Live podcast',
        '____ in that regard',
        'Guest Episode',
        'Douchebag guy',
        'Jake incorrectly guesses the theme of anonymous names',
        'They tell someone to break up',
        'Jake approves of Amir\'s intro',
        '"Momma turn down the podcast"',
        'Amir takes over 30 seconds to introduce the show',
        'They don\'t introduce the show for over 5 minutes after the theme song',
        'Jake talks shit about his dad',
        'One of them messes up reading a question',
        '"Haeeehhh!"',
        'Really obscure anonymous names',
        'J&A talk at the same time',
        'Something is coy',
        'Someone rhymes',
        'Jake shows appreciation for his dad\'s money',
        'Amir tries to divert attention from his middle name',
        'Jake professes his love for Amir, which is not returned',
        'Someone is "hard" or "jerking off right now"',
        'Jake gives advice having gotten laid in this same situation before',
        '"A dimepiece/10 cent coin/etc."',
        'Seemingly normal/mundane question that J&A jokingly mess with the guy for',
        'Amir gives math advice',
        'Amir tries to turn the question into tips for him getting laid, personally',
        '"Conundrum"',
        '"Sticky situation"',
        'Jake gives up mid-way through answering a question',
        'Jake sings alone',
        'J&A burst into song',
        'They speak in Eminem lyrics',
        'Someone gets put on blast',
        '"I resent the implication..."',
        'Jake gets depressed by the question',
        'The episode is hosted by Josh, Vance, or The Pinch',
        'Amir adds "-smith" to the end of an activity/occupation',
        'Tinder comes up',
        'They call themselves heroes',
        'Callback joke from a previous question',
        '"To that I say todah"',
        '"Todah"',
        'Amir tells someone to talk into the mic',
        'Yo do you',
        'Bonus Thursday episode',
        'Someone insults J&A in the question prompt',
]

free_ad = '"Things got real"'
ad_events = [
        '2 ads in 1 ad segment',
        'Only Amir telling the ad',
        '3+ ads in 1 episode',
        'They "Lose a sponsor" during an ad',
        'They jokingly advertise for something that is not a company (aka, bananas)',
        'Names/website shoutouts are read',
        'The ad pitch uses a rhyme',
        'Jake really forcing it',
        'They suggest website names/uses for the company\'s product',
        'They start the pitch using a song',
        'Naturebox',
        'Squarespace',
        'MeUndies',
        'Jake acts stupid during the pitch',
        'J&A jokingly call listeners losers/nerds/suckers/etc',
        'Jake takes the bit too far',
        'Amir repeats the name of the company at least 3 times in a row',
        'Dollar Shave Club',
        'Really unnatural mid-show ad break',
        'Promo code is something other than "Amir/Jake/ifiwereyou"',
        'Amir talks for over a full minute without Jake',
        'Jake uses an accent in the ad pitch',
        'Amir actually forgets to say "things got real"',
        'More time is spent during the break on ads than on talking during the break',
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
                    if 5*i+j == 12: #if at midpoint, write the default
                        row.append((j,data[0]))
                    else:
                        row.append((j,l[5*i + j]))
                except IndexError:
                    pass
            rows.append((i, row))
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
                'gamemode': gamemode,
        }
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/show', MainHandler),
    ('/theme', MainHandler),
    ('/ad', MainHandler),
    ('/', MainHandler),
], debug=True)

