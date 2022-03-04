from unittest import result
from flask import Blueprint, jsonify
from model.UserModel import User
from schema.UserSchema import users_schema

getListUserRoute = Blueprint('getListUserRoute',__name__)

@getListUserRoute.route('/getListUser',methods=['GET'])
def fun_get_user_list():
    result = User.query.all()
    return jsonify(users_schema.dump(result))
