from extension import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(100), nullable = False)
    address = db.Column(db.String(100), nullable = False)
    mobile = db.Column(db.Integer, nullable = False)
    typeorder = db.Column(db.String(100), nullable = False) 
    date = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = True)
    state = db.Column(db.String(100), nullable = False)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    product = db.relationship('OrderProduct',backref="order",lazy = True,uselist=True)
    
    