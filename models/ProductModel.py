from extension import db

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), unique = True)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)
    image_url = db.Column(db.String(100),nullable = True)
    type = db.Column(db.String(100))
    state = db.Column(db.Integer)
    order = db.relationship('OrderProduct',backref="product",lazy = True,uselist=True)