import logging
from random import randint
from flask import Flask, render_template, request, redirect
from flask_ask import Ask, statement, question, session, request
import urllib2
import json
import gitFeed
import techcrunch
import qod

app = Flask(__name__)
log = logging.getLogger()
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

newsList = []
numNews = len(newsList)

@ask.launch
def welcome():
    return question(render_template('welcome'))

@ask.intent('gitIntent')
def getGit():
    a = gitFeed.gitEvents()
    answer = a.getEvents()
    numAnswer = a.getCount()
    finalStatement = "You have " + str(numAnswer) + " new events. " + str(answer)
    return statement(finalStatement)

@ask.intent('techCrunchIntent')
def getTechCrunch():
    a = techcrunch.techNews()
    a.getNews()
    news = a.getList()
    count = a.getCount()
    finalStatement = ""
    for i in range(0, count):
        finalStatement += "Article Number " + str(i + 1) + ". " + news[i][0].encode('utf-8') + " "
    finalStatement += " Select one of " + str(count) + " choice to hear a description of the article"
    return question(finalStatement)

@ask.intent('inspirationIntent')
def getQuote():
    a = qod.QOD()
    return statement(a.getQuote())

@ask.intent('techCrunchChoiceIntent', convert={'number': int})
def getNews(number):
    a = techCrunch.techNews()
    a.getNews()
    news = a.getList()
    numNews = a.getCount()
    if number > numNews:
        return statement("Invalid choice. Choose again.")
    return statement(news[number][1].encode('utf-8') + ". More to be continued on the article.")



if __name__ == '__main__':
    app.run(debug=True)
