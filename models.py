from werkzeug import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """ User model class: data access layer """
    __tablename__ = 'users'
    uid = DB.Column(DB.Integer, primary_key=True)
    firstname = DB.Column(DB.String(100))
    lastname = DB.Column(DB.String(100))
    email = DB.Column(DB.String(120), unique=True)
    pwdhash = DB.Column(DB.String(54))

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        """ sets the password using a hash function """
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        """ checks the password hash """
        return check_password_hash(self.pwdhash, password)
