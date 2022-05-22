#1. import Flask
from flask import Flask

#2. create an app, being sure to pass __name__
app = Flask(__name__)

#3. define what to do when a user goes to the index route
@app.route('/')
def hello_world():
    return 'Hello world'