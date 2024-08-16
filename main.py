from user.services import create_user, read_user, update_user, delete_user

if __name__ == "__main__":
    # Example usage
    create_user("alice", "password123", True)
    print(read_user("alice"))
    update_user("alice", active=False)
    print(read_user("alice"))
    delete_user("alice")
    print(read_user("alice"))
