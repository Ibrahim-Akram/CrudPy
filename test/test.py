import unittest
from user.services import create_user, read_user, update_user, delete_user

class TestUserService(unittest.TestCase):

    def setUp(self):
        from user.repo import users
        users.clear()

    def test_create_user(self):
        user = create_user("alice", "password123", True)
        self.assertEqual(user.username, "alice")
        self.assertEqual(user.password, "password123")
        self.assertTrue(user.active)

    def test_read_user(self):
        create_user("bob", "password456", False)
        user = read_user("bob")
        self.assertEqual(user.username, "bob")

    def test_update_user(self):
        create_user("charlie", "password789", True)
        updated_user = update_user("charlie", password="newpassword", active=False)
        self.assertEqual(updated_user.password, "newpassword")
        self.assertFalse(updated_user.active)

    def test_delete_user(self):
        create_user("dave", "password000", True)
        delete_user("dave")
        self.assertIsNone(read_user("dave"))

if __name__ == "__main__":
    unittest.main()
