from flask import Blueprint, request
from extension import db
from models.ProductModel import Product
from models.UserModel import User
from schema.ProductSchema import product_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
deleteProductRoute = Blueprint("deleteProductRoute",__name__)

@deleteProductRoute.route('/delete/<id>',methods=['GET'])
def fun_delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)