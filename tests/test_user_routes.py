import pytest
from flask import url_for
from flask_testing import TestCase
from app import create_app, db
from app.models.user import User

class TestUserRoutes(TestCase):

    def create_app(self):
        return create_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_info_route(self):
        User.query.filter_by(email='test@example.com').delete()
        db.session.add(User(name='Test User', email='test@example.com'))
        db.session.commit()

        response = self.client.get(url_for('user_blueprint.user_info', userid=1))
        self.assert200(response)
        self.assertIn(b'Test User', response.data)

    def test_user_update_route(self):
        # Ensure there's no user with the same email
        User.query.filter_by(email='test@example.com').delete()
    
        # Add a user to update
        db.session.add(User(name='Test User', email='test@example.com'))
        db.session.commit()
    
        # Fetch the user to update
        user = User.query.filter_by(email='test@example.com').first()
        self.assertIsNotNone(user, "User should exist for update test")
    
        # Update the user
        response = self.client.put(
            url_for('user_blueprint.user_info', userid=user.userid),
            json={'name': 'Updated User'}
        )
    
        self.assert200(response)
        self.assertIn(b'User updated successfully', response.data)


# Add more test cases as needed
