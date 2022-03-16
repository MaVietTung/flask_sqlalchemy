from urllib import response
from flask import Blueprint, request
from sqlalchemy import null
from models.OrderModel import Order
from models.OrderProductModel import OrderProduct
from models.UserModel import User
from models.ProductModel import Product
from extension import db
from response import make_response
from schema.ProductSchema import product_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
routeAddProduct = Blueprint("routeAddProduct",__name__)

@routeAddProduct.route('/product',methods=['POST'])
def fun_add_product():
    name = request.json['name']
    owner = request.json['owner_id']
    image_url = request.json['image_url']
    type = request.json['type']
    state = request.json['state']
    order = request.json['order']
    price = request.json['price']
    new_product = Product(name = name,image_url = image_url,owner = User.query.get(owner),type = type , state = state)
    order = Order.query.get(order)
    if (order.price is None):
        order.price = price
    else:
        order.price += price
    productorder = OrderProduct(order = order, product = new_product,price = price)
    db.session.add(new_product)
    db.session.add(productorder)
    db.session.commit()
    result = product_schema.dump(new_product)
    response = make_response(header={"status code":200, "error code" : 0},data = result)
    return response