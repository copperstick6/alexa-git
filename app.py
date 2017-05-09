import logging
from random import randint
from flask import Flask, render_template, request, redirect
from flask_ask import Ask, statement, question, session, request
import urllib2
import json
import gitFeed
import techcrunch

app = Flask(__name__)
log = logging.getLogger()
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

newsList = []
numNews = len(newsList)

@ask.launch
def welcome():
    return question(render_template('welcome'))

@ask.intent('selectionIntent', convert={'choice':int})
def getChoice(choice):
    if choice == 1:
        a = gitFeed.gitEvents()
        answer = a.getEvents()
        numAnswer = a.getCount()
        finalStatement = "You have " + str(numAnswer) + " new events. " + answer
        return statement(finalStatement)
    elif choice == 2:
        a = techcrunch.techNews()
        a.getNews()
        global newsList
        newsList = a.getList()
        global numNews
        numNews = len(newsList)
        count = a.getCount()
        finalStatement = ""
        print newsList[0][0]
        for i in range(0, count):
            finalStatement += "Article Number " + str(i + 1) + ". " + newsList[i][0].encode('utf-8') + " "
        finalStatement += " Select one of " + str(count) + " choice to hear a description of the article"
        return question(finalStatement)

@ask.intent('techCrunchIntent', convert={'number': int})
def getNews(number):
    if number > numNews:
        return statement("Invalid choice. Choose again.")
    return statement(newsList[number][1].encode('utf-8') + ". More to be continued on the article.")



if __name__ == '__main__':
    app.run(debug=True)
