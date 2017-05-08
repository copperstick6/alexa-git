import logging
from random import randint
from flask import Flask, render_template, request, redirect
from flask_ask import Ask, statement, question, session, request
import urllib2
import json
import emailtext
import gitFeed

app = Flask(__name__)
log = logging.getLogger()
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def welcome():
    return question(render_template('welcome'))

@ask.intent('LoginIntent')
def displayCard():
    return question(render_template('login_please')).link_account_card()

if __name__ == '__main__':
    app.run(debug=True)
