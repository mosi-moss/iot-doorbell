from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_scss import Scss
import os
from flask_pywebpush import WebPush

# initialise app
app = Flask(__name__)
app.debug = True

# scss auto transpilation
app_dir = os.path.dirname(os.path.abspath(__file__))
assset_path = os.path.join(app_dir, "assets")
static_path = os.path.join(app_dir, "static")
Scss(app, static_dir = static_path, asset_dir = assset_path)

# a secret key used for secure data, such as passwords
app.config["SECRET_KEY"] = "super secret test key"
# sqlite database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# suppress track warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# webpush VAPID private key
app.config["WEBPUSH_VAPID_PRIVATE_KEY"] = "aTDyr6zDk6nivvU5COzSlpWFz572mRLrzYZ-b89YWjs"
# webpush info
app.config["WEBPUSH_SENDER_INFO"] = "mailto:admin@doorbell.net"

db = SQLAlchemy(app)
push = WebPush(app)

login_manager = LoginManager()
login_manager.init_app(app)

RESOLUTION = (640, 480)
FRAMERATE = None
BLINK_TIMES = 5

from doorbell.models import User
from doorbell import routes
