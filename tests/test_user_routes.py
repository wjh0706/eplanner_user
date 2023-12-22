import pytest
import json
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
    
    def test_create_user_route(self):
        # Define sample user data
        sample_user_data = {
            "name": "New User",
            "email": "newuser@example.com",
            "profile_picture": "path/to/picture.jpg"
        }

        # Make a POST request to the create user endpoint
        response = self.client.post(url_for('user_blueprint.user_create'), json=sample_user_data)

        # Assertions to ensure the endpoint behaves as expected
        self.assert200(response)
        self.assertIn(b'User created successfully', response.data)

        # Optionally, check if the user was indeed created in the database
        user = User.query.filter_by(email="newuser@example.com").first()
        self.assertIsNotNone(user, "New user should be created in the database")
