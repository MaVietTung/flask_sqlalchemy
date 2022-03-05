from flask import Blueprint, request
from extension import db
from models.UserModel import User
from schema.UserSchema import user_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
addUserRoute = Blueprint("addUserRoute",__name__)

@addUserRoute.route('/user',methods=['POST'])
def fun_add_user():
    name = request.json['name']
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)