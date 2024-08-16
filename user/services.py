# user_service/services.py

from user.data import users

def create_user(username, password, active):
    if username in users:
        raise ValueError('User already exists')
    users[username] = {'password': password, 'active': active}

def read_user(username):
    if username not in users:
        raise ValueError('User not found')
    return users[username]

def update_user(username, password=None, active=None):
    if username not in users:
        raise ValueError('User not found')
    if password is not None:
        users[username]['password'] = password
    if active is not None:
        users[username]['active'] = active

def delete_user(username):
    if username not in users:
        raise ValueError('User not found')
    del users[username]

def list_users():
    return [{'username': username, **details} for username, details in users.items()]
