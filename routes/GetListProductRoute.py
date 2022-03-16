from flask import Blueprint, jsonify, render_template
from response import make_response
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
    response = make_response(header={"status code":200,"error code":0},data = result)
    return response