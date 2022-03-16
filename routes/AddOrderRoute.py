from flask import Blueprint, request
from extension import db
from models.OrderModel import Order
from models.UserModel import User
from response import make_response
from schema.OrderSchema import order_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
addOrderRoute = Blueprint("addOrderRoute",__name__)

@addOrderRoute.route('/order',methods=['POST'])
def fun_add_user():
    description = request.json['description']
    address = request.json['address']
    mobile = request.json['mobile']
    typeorder = request.json['typeorder']
    date = request.json['date']
    if("price" in request.json):
        price = request.json['price']
    else:
        price = None
    state = request.json['state']
    owner = request.json['owner']
    order = Order(description = description, address = address, mobile = mobile, typeorder = typeorder , date = date, price = price , state = state, owner = User.query.get(owner))
    db.session.add(order)
    db.session.commit()
    result = order_schema.dump(order)
    response = make_response(header={"status code":200},data = result)
    return response