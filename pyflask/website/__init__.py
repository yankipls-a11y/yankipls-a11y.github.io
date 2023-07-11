#initialize Flash
from flask import Flask

def create_app():
    app = Flask(__name__) #name represents file name 
    app.config['SECRET_KEY'] = 'secret69' #encrypts session data and cookies related to the website

    return app