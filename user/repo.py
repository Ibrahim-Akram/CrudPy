users = []

def add_user(user):
    users.append(user)

def get_user(username):
    for user in users:
        if user.username == username:
            return user
    return None

def remove_user(username):
    global users
    users = [user for user in users if user.username != username]
