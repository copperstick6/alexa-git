import urllib2
import json
qodURL = "http://quotes.rest/qod.json"
class QOD():
    def getQuote(self):
        webURL = urllib2.urlopen(qodURL)
        resultString = "The quote of the day is: "
        if webURL.getcode() == 200:
            data = webURL.read()
            result = json.loads(data)
            resultString += result['contents']['quotes'][0]['quote']
            resultString += " Quote by " + result['contents']['quotes'][0]['author']
            return resultString
        else:
            return "There was an error with the API call."
