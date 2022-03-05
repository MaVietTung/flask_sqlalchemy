from flask import Blueprint, request
from models.UserModel import User
from models.ProductModel import Product
from extension import db
from schema.ProductSchema import product_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
routeAddProduct = Blueprint("routeAddProduct",__name__)

@routeAddProduct.route('/product',methods=['POST'])
def fun_add_product():
    name = request.json['name']
    price = request.json['price']
    owner = request.json['owner_id']
    new_product = Product(name = name,price = price,owner = User.query.get(owner))
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)