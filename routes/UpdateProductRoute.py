import email
from math import prod
import re
from urllib import response
from flask import Blueprint, request
from extension import db
from models.ProductModel import Product
from models.UserModel import User
from response import make_response
from schema.ProductSchema import product_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
updateProductRoute = Blueprint("updateProductRoute",__name__)

@updateProductRoute.route('/update/<id>',methods=['PUT'])
def fun_update(id):
    product = Product.query.get(id)
    if("name" in request.json):
        name = request.json['name']
        product.name = name
    if("state" in request.json):
        state = request.json['state']
        product.state = state
    if("age" in request.json):
        age = request.json['age']
        product.age = age
    if("email" in request.json):
        email = request.json['email']
        product.email = email
    if("type" in request.json):
        type = request.json['type']
        product.type = type
    if("owner_id" in request.json):
        owner = request.json['owner_id']
        product.owner = User.query.get(owner)
    db.session.commit()
    response =  make_response(product_schema.dump(product))
    return response