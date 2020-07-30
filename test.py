from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from datetime import datetime
from pprint import pprint
import model
import requests
import json

load_dotenv()

app = Flask(__name__)
app.jinja_env.globals['current_time'] = datetime.now()

MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD")

app.config['MONGO_DBNAME'] = MONGO_DBNAME
app.config['MONGO_URI'] = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@user-game-data.yi30k.mongodb.net/{MONGO_DBNAME}?retryWrites=true&w=majority'

mongo = PyMongo(app)

mongo.db.games.remove({"name": "Cell to Singularity - Evolution Never Ends"})