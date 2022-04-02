from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# a secret key used for secure data, such as passwords
app.config["SECRET_KEY"] = "super secret test key"
# sqlite database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# suppress track warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from doorbell.models import User
from doorbell import routes