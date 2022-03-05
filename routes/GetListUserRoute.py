from unittest import result
from flask import Blueprint, jsonify
from models.UserModel import User
from schema.UserSchema import users_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
getListUserRoute = Blueprint('getListUserRoute',__name__)

@getListUserRoute.route('/getListUser',methods=['GET'])
def fun_get_user_list():
    result = User.query.all()
    return jsonify(users_schema.dump(result))
