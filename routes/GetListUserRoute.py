from email.quoprimime import header_decode
from unittest import result
from urllib import response
from flask import Blueprint, jsonify
from models.UserModel import User
from response import make_response
from schema.UserSchema import users_schema

"""Represents a blueprint, a collection of routes and other
    app-related functions that can be registered on a real application
    later."""
getListUserRoute = Blueprint('getListUserRoute',__name__)

@getListUserRoute.route('/getListUser',methods=['GET'])
def fun_get_user_list():
    result = User.query.all()
    result = users_schema.dump(result)
    response = make_response(header={"status_code":200,"error code":0},data=result)
    return response
