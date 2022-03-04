from flask import Blueprint
from schema.ProductSchema import product_schema
from model.ProductModel import Product

getProductByIDRoute = Blueprint("getProductByIDRoute",__name__)

@getProductByIDRoute.route('/product/<id>',methods=['GET'])
def fun_get_by_id(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)