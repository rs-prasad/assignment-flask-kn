import datetime
from .. import db
from geoalchemy2.types import Geometry
from geoalchemy2.elements import WKTElement
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError


class UserPost(db.Model):

    __tablename__ = 'posts_table'
    id = db.Column(db.Integer, primary_key=True,index=True)

    username = db.Column(db.String(64),)

    text = db.Column(db.String(1000),
                     nullable=False)
    lon = db.Column(db.Float,nullable=False)
    lat = db.Column(db.Float,nullable=False)
   

    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def put_post_in_db(id, username, text, lat, lon):
        new_user_post = UserPost(id=id, username=username,
                                 text=text,lat=lat,lon=lon)
        db.session.add(new_user_post)
        try:
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            return e


    @staticmethod
    def get_last_id():
        return db.session.query(func.max(UserPost.id)).scalar()

    @staticmethod
    def fetch_all_posts():
        return UserPost.query.all()