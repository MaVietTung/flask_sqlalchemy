from flask import Blueprint, jsonify
from models.OrderModel import Order
from models.UserModel import User
from response import make_response
from schema.OrderSchema import orders_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
getListOderRoute = Blueprint('getListOderRoute',__name__)

@getListOderRoute.route('/getListOrder',methods=['GET'])
def fun_get_order_list():
    result = Order.query.all()
    result = orders_schema.dump(result)
    response = make_response(header={"status_code":200,"error code":0},data=result)
    return response
