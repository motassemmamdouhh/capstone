import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
# deploying a local database to test the app localy

#database_path= 'postgresql://postgres:77288399@localhost:5432/casting'
#altering database path for heroku deployment

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer(), primary_key=True)
    title  = db.Column(db.String())
    release_date = db.Column(db.String())

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
    def format(self):
        return{
            'id': self.id,
            'title' : self.title,
            'release date' : self.release_date
        }
    
class Actor(db.Model):
    __tablename__ = "actors"
    id  = db.Column(db.Integer(), primary_key= True)
    name= db.Column(db.String(120))
    age= db.Column(db.Integer())
    gender=db.Column(db.String(120))

    def __init__(self, name, age, gender):
        self.name = name
        self.age= age
        self.gender= gender

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
    def format(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "age" : self.age,
            "gender" : self.gender
        }