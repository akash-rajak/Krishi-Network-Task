
# imported necessary libraries
from flask import jsonify, request, flash
import datetime
from sqlalchemy import func
from apps.post.models import Post
from dbfile import db
import timeago
from werkzeug.exceptions import HTTPException


# function defined for get post, this also using exception handling
def getPost():
   try:
      args = request.args
      # got the latitude and longitude via requests
      lat = str(args.get('lat'))
      lon = str(args.get('lon'))

      db1 = db.session.query(Post.message,Post.location,Post.created_on).order_by(func.ST_Distance(Post.location,func.Geometry(func.ST_GeomFromText('POINT({} {})'.format(lon, lat))))).all()

      l=[{"message":i.message,"location":str(i.location),"created_on":timeago.format(datetime.datetime.now(),i.created_on)} for i in db1]
      obj={}
      obj["success"]=True
      obj['results'] = l[0:10]
      return jsonify(obj),200
   except Exception as e:
      raise Exception("Error Occurred")



# function defined to create Post, using exception handling
def createPost():
   try:
      form=request.get_json()
      employee = Post(message=form["message"], location='POINT('+form["location"]+')')
      db.session.add(employee)
      db.session.commit()
      db.session.refresh(employee)
      db.session.commit()
      flash("Empoyee addition is successful")
      return jsonify({'success': True}),200
   except Exception as e:
      raise Exception("Error Occurred")
