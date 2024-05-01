from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from website.mydb import users
from bson import ObjectId
from .auth import views
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin'
    
    
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix='/')

    return app        


