from flask import Blueprint, jsonify
from models.OrderModel import Order
from models.OrderProductModel import OrderProduct
from models.UserModel import User
from response import make_response
from schema.ProductSchema import products_schema
from schema.OrderSchema import orders_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
getListProductByOrderIdRoute = Blueprint('getListProductByOrderIdRoute',__name__)

@getListProductByOrderIdRoute.route('/getListOderByOrderIdRoute/<id>',methods=['GET'])
def fun_get_order_list(id):
    result = OrderProduct.query.filter_by(order_id = id).all()
    result = products_schema.dump(i.product for i in result)
    response = make_response(header={"status_code":200,"error code":0},data=result)
    return response