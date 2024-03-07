from flask import Flask
from config import Config
from flask_login import LoginManager
from app.models import db, User
from flask_migrate import Migrate
from flask_moment import Moment
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

login_manager = LoginManager()

login_manager.init_app(app)
db.init_app(app)
migrate = Migrate(app, db)
moment = Moment(app)



from app.blueprints.auth import auth


app.register_blueprint(auth)


@login_manager.user_loader
def loadUser(userID):
    return User.query.get(userID)