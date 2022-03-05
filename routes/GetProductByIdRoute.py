from flask import Blueprint
from schema.ProductSchema import product_schema
from models.ProductModel import Product

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
getProductByIDRoute = Blueprint("getProductByIDRoute",__name__)

@getProductByIDRoute.route('/product/<id>',methods=['GET'])
def fun_get_by_id(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)