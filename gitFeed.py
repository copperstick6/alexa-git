import urllib2
import json
import time

gitUrl = "https://api.github.com/users/copperstick6/received_events"

class gitEvents():
    def __init__(self):
        idFile = open('id.txt', 'r')
        self.lastID = idFile.readline()
        idFile.close()


    def changeID(self, id):
        idFile = open('id.txt', 'w')
        idFile.write(str(id))
        idFile.close()
        return id

    def getID(self):
        return self.lastID

    def getEvents(self):
        webUrl = urllib2.urlopen(gitUrl)
        resultString = ""
        if webUrl.getcode() == 200:
            data = webUrl.read()
            result = json.loads(data)
            #I want the first 5 results, don't want my ears blasted with BS
            if int(result[0]['id']) == int(self.lastID):
                return "No Results found"
            else:
                counter = 0
                for i in range (0, 3):
                    if result[i]['id'] == int(self.lastID):
                        break
                    else:
                        counter +=1
                        resultString += "Event type " + result[i]['type'] + ". User " + result[i]['actor']['display_login'] + ". Repo " + result[i]['repo']['name'] + ". "
                tempString = "There are " + str(counter) + " results. " + resultString
                idFile = open('id.txt', 'w')
                idFile.write(str(result[0]['id']))
                idFile.close()
                return tempString


a = gitEvents()
print a.getEvents()
