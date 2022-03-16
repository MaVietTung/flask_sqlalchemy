from flask import jsonify


def make_response(header={},data={}):
    response = header
    response["data"] = data
    return jsonify(response)
