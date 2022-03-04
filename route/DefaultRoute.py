from flask import Blueprint, jsonify
from schema.ProductSchema import product_schema

defaultRoute = Blueprint("defaultRoute",__name__)

@defaultRoute.route('/',methods=['GET'])
def fun_default():
    return jsonify({'msg':'Hello Newebie'})