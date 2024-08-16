import unittest
import json
from app import app  # Import your Flask app from app.py

class UserCrudTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        # Test the user creation endpoint
        response = self.app.post('/users', 
            data=json.dumps({
                'username': 'alice',
                'password': 'password123',
                'active': True
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'alice', response.data)

    def test_read_user(self):
        # First, create a user
        self.app.post('/users', 
            data=json.dumps({
                'username': 'alice',
                'password': 'password123',
                'active': True
            }),
            content_type='application/json'
        )
        # Test the user read endpoint
        response = self.app.get('/users/alice')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'alice', response.data)

    def test_update_user(self):
        # First, create a user
        self.app.post('/users', 
            data=json.dumps({
                'username': 'alice',
                'password': 'password123',
                'active': True
            }),
            content_type='application/json'
        )
        # Test the user update endpoint
        response = self.app.put('/users/alice', 
            data=json.dumps({
                'active': False
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'false', response.data)

    def test_delete_user(self):
        # First, create a user
        self.app.post('/users', 
            data=json.dumps({
                'username': 'alice',
                'password': 'password123',
                'active': True
            }),
            content_type='application/json'
        )
        # Test the user deletion endpoint
        response = self.app.delete('/users/alice')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User deleted', response.data)

    def test_user_not_found(self):
        # Test the read endpoint for a user that doesn't exist
        response = self.app.get('/users/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'User not found', response.data)

if __name__ == '__main__':
    unittest.main()
