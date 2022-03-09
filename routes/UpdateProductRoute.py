from urllib import response
from flask import Blueprint, request
from extension import db
from models.ProductModel import Product
from models.UserModel import User
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
    if("price" in request.json):
        price = request.json['price']
        product.price = price
    if("owner_id" in request.json):
        owner = request.json['owner_id']
        product.owner = User.query.get(owner)
    db.session.commit()
    response = product_schema.jsonify(product)
    response.status_code = 200
    response.content_type = "aplication/json"
    response.headers['Custom-header'] = "Custom-header"
    return response