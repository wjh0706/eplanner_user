from flask_testing import TestCase
from app import create_app, db
from app.models.user import User
from app.services.user_service import get_user_info, update_user_info

class TestUserService(TestCase):

    def create_app(self):
        # Make sure this returns a Flask app instance with testing configuration
        return create_app()

    def setUp(self):
        db.create_all()
        # Create a user for testing
        test_user = User(name='Test User', email='test@example.com')
        db.session.add(test_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_user_info(self):
        # Assuming the first user has a userid of 1
        user_info = get_user_info(1)
        self.assertEqual(user_info['name'], 'Test User')
        self.assertEqual(user_info['email'], 'test@example.com')

    def test_update_user_info(self):
        new_data = {'name': 'Updated Name', 'email': 'updated@example.com'}
        response = update_user_info(1, new_data)
        self.assertEqual(response['message'], 'User updated successfully')

        # Fetch the updated user and check the updated fields
        updated_user = db.session.get(User, 1)
        self.assertEqual(updated_user.name, 'Updated Name')
        self.assertEqual(updated_user.email, 'updated@example.com')

# To run tests if this script is executed directly
if __name__ == '__main__':
    import unittest
    unittest.main()
