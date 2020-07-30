from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from datetime import datetime
import model
import requests

load_dotenv()
# -- Initialization section --

app = Flask(__name__)
app.jinja_env.globals['current_time'] = datetime.now()
# -- Initialization section --

MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD")
#
app.config['MONGO_DBNAME'] = MONGO_DBNAME
app.config['MONGO_URI'] = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@user-game-data.yi30k.mongodb.net/{MONGO_DBNAME}?retryWrites=true&w=majority'
mongo = PyMongo(app)

app.jinja_env.globals['current_time'] = datetime.now()

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())

@app.route('/game_recs', methods=["GET","POST"])
def game_recs():
    if request.method == 'GET':
        return redirect(url_for("index"))
    else:
        form = request.form
        console = form["console"]
        genre = form["genre"]
        games = model.get_games(console, genre)
        """
        event = {
        'name':form['eventName'],
        'date':form['eventDate'],
        }

        events = mongo.db['events-list']
        events.insert(event)
        """
        return render_template("game_recs.html", games=games, model=model, time=datetime.now())
