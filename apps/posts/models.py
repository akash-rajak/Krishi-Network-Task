
# imported necessary library
import datetime
from dbfile import db
from geoalchemy2 import Geometry


# created class Post with database model as an argument
class Post(db.Model):
   __tablename__ = 'post'
   id = db.Column(db.Integer(), primary_key = True)
   message = db.Column(db.String)
   location = db.Column(Geometry(geometry_type='POINT'))
   # active = db.Column(db.Boolean, default=True)
   created_on = db.Column(db.DateTime, default=datetime.datetime.now())

   def __init__(self, message,location=None):
      self.message = message
      self.location = location