from venv import create
from extension import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(100))
    state = db.Column(db.String(100))
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    create = db.Column(db.DateTime) 
