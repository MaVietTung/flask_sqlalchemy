from extension import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique = True)
    age = db.Column(db.Integer,unique = True)
    address = db.Column(db.String(100),unique= True)
    mobile = db.Column(db.Integer,unique = True)
    email = db.Column(db.String(100),unique = True)
    """
        product attribute define relation ship between User and Product Table,
         method relationship has parameter uselist = True(By default), 
        it mean one-to-many relationship, 
        'backref' define attribute will be call from Product instance for referrence User instance, 
        for example:
        product  = Product(...)
        product.owner = User(...)
    """
    product = db.relationship('Product',backref='owner',lazy=True)
    order = db.relationship('Order',backref='owner',uselist = True,lazy= True)
    report = db.relationship('Report',backref='owner',uselist = True, lazy = True)