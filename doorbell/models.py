from doorbell import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import json

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique = True, nullable = False)
    password_hash = db.Column(db.String(128))
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.username}')"

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subscription_info = db.Column(db.Text())
    is_active = db.Column(db.Boolean(), default=True)