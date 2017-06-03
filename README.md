# alexa-git   
Just another one of my crazy ideas.    
Easy and simple mornings. Listen to TechCrunch, and chill out to your git feed updates.

## Setup    
I'll be providing two methods of setup, one locally, the other one by using zappa to deploy to AWS.

# Deploying to AWS via Zappa:  
1. In order to deploy to via zappa, you need to make a virtual environment. Create one via the command virtualenv venv.  

2. After creating the virtual environment, you need to cd into the venv directory by running the command cd venv.   

3. Then, you need to install dependencies. You need to install flask-ask, zappa, and awscli. sudo pip install flask-ask zappa awscli. If you get an error, install all dependencies but awscli and run the command sudo -H pip install awscli --upgrade --ignore-installed six to install awscli.   

4. Make sure the venv is up and running, then run the command aws configure. After running that command, make sure to get the proper credentials from the AWS IAM console. After getting those credentials, put it into your terminal via plaintext and make sure to confirm all defaults, unless you want to run your aws console on some other server other than us-east-1.  

5. Move all the fies into your the directory with the venv folder. This is the code that will be run.  

6. Don't forget to grab your API keys.  
You need to first create a keys.py file which will store your API keys and Git usernames. Grab a newsapi key [here](https://newsapi.org/techcrunch-api). Create two methods, one called techAPI, and the other called gitUsername. Below is an example:  
```
def gitUsername():
  return "copperstick6"
def techAPI():
  return "yourAPIKeyHere"
```


7. Afterwards, run zappa init. This will get your server initialized. Make sure that zappa knows what the entry point of the program is and also make sure to call your program something, I've called it dev.  

8. After running zappa init, make sure to deploy it. Run zappa deploy dev.


# Running The Server Locally:

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
