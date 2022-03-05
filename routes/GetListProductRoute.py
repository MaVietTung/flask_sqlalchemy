from flask import Blueprint, jsonify

from models.ProductModel import Product
from schema.ProductSchema import products_schema

routeListProduct = Blueprint("routeListProduct",__name__)

@routeListProduct.route('/getListProduct',methods=['GET'])
def fun_get_list_product():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)