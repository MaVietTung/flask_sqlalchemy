import datetime
from email.policy import default
from flask import Flask,request,jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from config import *
import os

#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#database config

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
#init db 
db = SQLAlchemy(app)
    

#init ma
ma = Marshmallow(app)


#Model/Class
class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), unique = True)
    price = db.Column(db.Integer)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = True)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique = True)
    product = db.relationship('Product', uselist=False, backref="user")


#Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','price','onwer_id')
#User Scheama
class UserSchema(ma.Schema):
    class Meta:
        fields= ('id','name')
#init schema
product_schema  = ProductSchema()
products_schema = ProductSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

#set route
@app.route('/',methods=['GET'])
def fun_default():
    return jsonify({'msg':'Hello Newebie'})
@app.route('/product',methods=['POST'])
def fun_add_product():
    name = request.json['name']
    price = request.json['price']
    owner = request.json['owner_id']
    owner = User.query.get(owner)
    new_product = Product(name=name,price=price,user=owner)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)
@app.route('/getListProduct',methods=['GET'])
def fun_get_list_product():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)
@app.route('/update/<id>',methods=['PUT'])
def fun_update(id):
    product = Product.query.get(id)
    name = request.json['name']
    price = request.json['price']
    owner = request.json['owner_id']
    product.owner = User.query.get(owner)
    product.name = name
    product.price = price
    product.owner = User.query.get(owner)
    db.session.commit()
    return product_schema.jsonify(product)
@app.route('/product/<id>',methods=['GET'])
def fun_get_by_id(id):
    product = Product.query.get(id)
    user = User.query.get(product.owner_id)
    print(user.name)
    return product_schema.jsonify(product)
@app.route('/user',methods=['POST'])
def fun_add_user():
    name = request.json['name']
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)

#run server
if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug = True)

