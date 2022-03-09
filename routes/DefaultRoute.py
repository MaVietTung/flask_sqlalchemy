from urllib import response
from flask import Blueprint, jsonify
from schema.ProductSchema import product_schema

defaultRoute = Blueprint("defaultRoute",__name__)

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
@defaultRoute.route('/',methods=['GET'])
def fun_default():
    response = jsonify({'msg':'Hello Newebie'})
    response.status_code = 200
    response.content_type = "aplication/json"
    response.headers['Custom-header'] = "Custom-header"
    return response