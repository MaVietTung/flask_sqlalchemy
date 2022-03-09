from flask import Blueprint, jsonify, make_response, render_template

from models.ProductModel import Product
from schema.ProductSchema import products_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
routeListProduct = Blueprint("routeListProduct",__name__)

@routeListProduct.route('/getListProduct',methods=['GET'])
def fun_get_list_product():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    response = jsonify(result)
    response.status_code = 200
    response.content_type = "aplication/json"
    response.headers['Custom-header'] = "Custom-header"
    return response