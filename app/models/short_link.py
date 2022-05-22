from datetime import datetime
from app import db

# Alias common DB names
Column = db.Column
Model = db.Model
relationship = db.relationship

class ShortLink(Model):
    """ User model for storing user related data """

    shortId = Column(db.String(10), primary_key=True)
    url = Column(db.String(1000), unique=True)
    createdAt = Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super(ShortLink, self).__init__(**kwargs)