import keys
import urllib2
import json

baseUrl = "https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=" + keys.techAPI()

class techNews():
    def __init__(self):
        self.count = 0
        self.news = []

    def getList(self):
        return self.news

    def getCount(self):
        return self.count

    def getNews(self):
        webUrl = urllib2.urlopen(baseUrl)
        resultString = ""
        if webUrl.getcode() == 200:
            data = webUrl.read()
            result = json.loads(data)
            for i in range(0, int(len(result['articles']))):
                tempList = [result['articles'][i]['title'], result['articles'][i]['description']]
                self.news.append(tempList)
            self.count = int(len(result['articles']))
