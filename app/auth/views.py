from flask import jsonify, request
from app import app, auth_controller


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    result = auth_controller.register_user(data.get('username'), data.get('password'))
    return jsonify(result)
