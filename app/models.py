from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


    def __init__(self, first_name, last_name, email, username, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.phone_number = phone_number
        self.password = generate_password_hash(password)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
class JobLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.Integer, unique=True, nullable=False)
    city = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Integer, nullable = False)
    zipcode = db.Column(db.Integer, nullable=False)
    up_votes = db.Column(db.Integer)
    down_votes = db.Column(db.Integer)


    def __init__(self, street, city, state, zipcode, up_votes, down_votes):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.up_votes = up_votes
        self.down_votes = down_votes

    def save(self):
        db.session.add(self)
        db.session.commit()


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable = False)
    job_location_id = db.Column(db.Integer, db.ForeignKey('job_location.id'), nullable=False)

    def __init__(self, title, body, job_description_id):
        self.title = title
        self.body = body
        self.job_Location_id = job_description_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()
