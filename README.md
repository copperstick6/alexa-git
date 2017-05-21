# alexa-git   
Just another one of my crazy ideas.    
Easy and simple mornings. Listen to TechCrunch, and chill out to your git feed updates.
  
## Setup    
I'll be adding lambda support in v2.  
### Step 1: Clone the Repo    

### Step 2: Grab your API keys   
You need to first create a keys.py file which will store your API keys and Git usernames. Grab a newsapi key [here](https://newsapi.org/techcrunch-api). Create two methods, one called techAPI, and the other called gitUsername. Below is an example:   
```
def gitUsername():
  return "copperstick6"
def techAPI():
  return "yourAPIKeyHere"
``` 

### Step 3: Run the server   
This utilizes python2.7. Make sure to pip install -r requirements.txt to install requirements and then open up a console and type the command python app.py to run the server locally

### Step 4: Use Ngrok to create a tunnel to localhost so that Alexa can make requests to your server   
Run ./ngrok http 5000 in console on mac. IDK what it is on windows.   

### Step 5: Set up your Alexa App on the Amazon Developer's Console
Create a new Alexa app through the Amazon Developer Console. Name it whatever you want, invocation name is how you will run the app.    
Go to interaction model (click next). Copy the contents of interactionmodel.txt and paste it into the first box, called intent schema. Copy the contents of utterances.txt and paste it into the third box, called sample utterances. This is how Alexa will respond/choose what method to call. Click Next.  
The Configuration is pretty important. Click HTTPS and North America, and copy the ngrok.io link found in your console that's running the ./ngrok command. It should be next to forwarding. Paste it into the box under North America. Click Next.  

### Step 6: You're all done! Test via echosim.io or test via your own Alexa!

sudo -H pip install awscli --upgrade --ignore-installed six
