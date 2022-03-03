from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Model/Class
class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), unique = True)
    price = db.Column(db.Integer)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = True)



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique = True)
    """
    delete uselist = False in db.relationship mean we set up relation type one-to-many(one user is  the owner of many product)
    Now we set up type one-to-one relationship
    """
    product = db.relationship('Product',backref='owner',lazy=True)



"""
>>> user = User('tung') 
>>> product = Product('may tinh',100000) 
>>> product.onwer = user 
>>> product.onwer
<User (transient 1994422025760)>
>>> product.onwer.name
'tung'
>>>
"""

"""
many-to-many relation ship

user-product = db.Table(
    db.Column('column_id',db.Integer,db.ForeignKey('column.id')),
    db.Column('user_id',db.Integer,db.ForeignKey(user.id))
)

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), unique = True)
    price = db.Column(db.Integer)
    onwer = db.relationship('User',secondary=user-product,backref='onwee')
    def __init__(self,name,price):
        self.name = name
        self.price = price


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique = True)
    db.relationship('Product',secondary=user-product,backref='onwer',lazy=True,uselist=False)
    def __init__(self,name):
        self.name=name

user = User(...)
product = Product(...)

user.onwer.append[user]
product.onwee.append[product]

"""