from unittest import result
from urllib import response
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
    response = jsonify(users_schema.dump(result))
    response.status_code = 200
    response.content_type = "aplication/json"
    response.headers['Custom-header'] = "Custom-header"
    return response
