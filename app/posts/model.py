import datetime
from .. import db
from geoalchemy2.types import Geometry
from geoalchemy2.elements import WKTElement


class UserPost(db.Model):

    __tablename__ = 'posts_table'
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), unique=False,
                         nullable=False, index=False)

    text = db.Column(db.String(1000),
                     nullable=False, index=False)

    location = db.Column(Geometry('POINT'))

    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def put_post_in_db(id, username, text, lat, lon):
        location = WKTElement(
            'POINT({0} {1})'.format(lon, lat), srid=4326)
        new_user_post = UserPost(id=id, username=username,
                                 text=text, location=location)
        db.session.add(new_user_post)
        db.session.commit()
