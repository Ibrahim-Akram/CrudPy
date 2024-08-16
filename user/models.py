class User:
    def __init__(self, username, password, active):
        self.username = username
        self.password = password
        self.active = active

    def __repr__(self):
        return f"User(username={self.username}, active={self.active})"
