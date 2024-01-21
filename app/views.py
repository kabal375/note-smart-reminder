from flask import jsonify, request
from app import app, controllers


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    result = controllers.register_user(data.get('username'), data.get('password'))
    return jsonify(result)
