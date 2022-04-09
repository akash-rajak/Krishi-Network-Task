
# impoted necessary library
from apps import app
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

from dbfile import db
from apps.post.routes import post_bp
from apps.weather.routes import weather_bp
from apps.utility.controller import handle_exception,handle_Hexception

# flask started
app = Flask(__name__)
uri=os.getenv("DB_URI")
key=os.getenv("S_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] = key

db.init_app(app)

app.register_blueprint(post_bp, url_prefix='/api')
app.register_blueprint(weather_bp, url_prefix='/api')


# main function defined from where the app runs
if __name__ == '__main__':
  app.run()
  
    
