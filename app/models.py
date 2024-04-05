from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from secrets import token_hex

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    token = db.Column(db.String)


    def __init__(self, first_name, last_name, email, company_name, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.company_name = company_name
        self.phone_number = phone_number
        self.password = generate_password_hash(password)
        self.token = token_hex(16)

    def to_dict(self):
        return {
            "user_id": self.id,
            "company_name": self.company_name,
            "email": self.email,
            "token": self.token,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
class JobLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formatted_address = db.Column(db.String, nullable=False)

    def __init__(self, formatted_address):
        self.formatted_address = formatted_address

    def save(self):
        db.session.add(self)
        db.session.commit()


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable = False)
    client_first_name = db.Column(db.String, nullable = False)
    client_last_name = db.Column(db.String, nullable = False)
    job_location_id = db.Column(db.Integer, db.ForeignKey('job_location.id'), nullable=False)
    date = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)

    def __init__(self, user_id, title, date, client_first_name, client_last_name, body, job_location_id, rating):
        self.title = title
        self.user_id = user_id
        self.body = body
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.rating = rating
        self.date = date
        self.job_location_id = job_location_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()
