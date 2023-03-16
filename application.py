from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello World. Updating the message for the world. This message is from your Lord, Hensen Dumfry.'