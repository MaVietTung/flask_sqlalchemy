from extension import db

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), unique = True)
    price = db.Column(db.Integer)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = True)