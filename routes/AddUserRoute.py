from flask import Blueprint, request
from extension import db
from models.UserModel import User
from response import make_response
from schema.UserSchema import user_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
addUserRoute = Blueprint("addUserRoute",__name__)

@addUserRoute.route('/user',methods=['POST'])
def fun_add_user():
    name = request.json['name']
    age = request.json['age']
    mobile = request.json['mobile']
    email = request.json['email']
    address = request.json['address']
    user = User(name=name, age = age, mobile = mobile, email = email,address = address)
    db.session.add(user)
    db.session.commit()
    result = user_schema.dump(user)
    response = make_response(header={"status code":200},data = result)
    return response