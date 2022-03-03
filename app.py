from enum import unique
from unittest import result
from flask import Flask,request,jsonify
from flask_marshmallow import Marshmallow
import os

#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#database config
from config import *
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
#init db 
from model import *
db.init_app(app)
with app.app_context():
    #db.drop_all()
    db.create_all()

#init ma
from schema import *
ma.init_app(app)


#set route
@app.route('/',methods=['GET'])
def fun_default():
    return jsonify({'msg':'Hello Newebie'})
@app.route('/product',methods=['POST'])
def fun_add_product():
    name = request.json['name']
    price = request.json['price']
    owner = request.json['owner_id']
    new_product = Product(name = name,price = price,owner = User.query.get(owner))
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
    if("name" in request.json):
        name = request.json['name']
        product.name = name
    if("price" in request.json):
        price = request.json['price']
        product.price = price
    if("owner_id" in request.json):
        owner = request.json['owner_id']
        product.owner = User.query.get(owner)
    db.session.commit()
    return product_schema.jsonify(product)
@app.route('/product/<id>',methods=['GET'])
def fun_get_by_id(id):
    product = Product.query.get(id)
    print(product.owner_id)
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
    app.run(debug = True)

