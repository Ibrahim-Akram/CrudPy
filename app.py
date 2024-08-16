# app.py

from flask import Flask, request, jsonify, render_template
from user.services import create_user, read_user, update_user, delete_user, list_users

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def list_users_route():
    try:
        users = list_users()
        return jsonify(users)
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    username = data['username']
    password = data['password']
    active = data['active']
    try:
        create_user(username, password, active)
        return jsonify({'message': 'User created successfully!'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/users/<username>', methods=['PUT'])
def update_user_route(username):
    data = request.get_json()
    password = data.get('password')
    active = data.get('active')
    try:
        update_user(username, password=password, active=active)
        return jsonify({'message': 'User updated successfully!'})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/users/<username>', methods=['DELETE'])
def delete_user_route(username):
    try:
        delete_user(username)
        return jsonify({'message': 'User deleted successfully!'})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
