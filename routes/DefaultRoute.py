from flask import Blueprint, jsonify
from schema.ProductSchema import product_schema

defaultRoute = Blueprint("defaultRoute",__name__)

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
@defaultRoute.route('/',methods=['GET'])
def fun_default():
    return jsonify({'msg':'Hello Newebie'})