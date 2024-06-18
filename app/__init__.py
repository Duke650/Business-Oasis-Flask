# app/__init__.py

from flask import Flask
from config import Config
from app.models import db, User
from flask_migrate import Migrate
from flask_moment import Moment
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
migrate = Migrate(app, db)
moment = Moment(app)

from app.blueprints.auth import auth
from app.blueprints.reviews import reviews
from app.blueprints.jobLocation import jobLocation
from app.blueprints.proxy.proxy import proxy_bp 


app.register_blueprint(auth)
app.register_blueprint(reviews)
app.register_blueprint(jobLocation)
app.register_blueprint(proxy_bp)

