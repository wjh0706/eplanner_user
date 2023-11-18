import pytest
from app import create_app, db
from app.models.user import User
from app.services.user_service import get_user_info, update_user_info

@pytest.fixture(scope='module')
def test_app():
    app = create_app()  # Create a Flask app with testing configuration
    app_context = app.app_context()
    app_context.push()

    db.create_all()  # Create a new database for the tests

    yield app  # testing happens here

    db.session.remove()
    db.drop_all()
    app_context.pop()

@pytest.fixture(scope='module')
def test_user(test_app):
    user = User(name='Test User', email='test@example.com')
    db.session.add(user)
    db.session.commit()
    return user

def test_get_user_info(test_app, test_user):
    user_info = get_user_info(test_user.userid)
    assert user_info['name'] == 'Test User'
    assert user_info['email'] == 'test@example.com'

def test_update_user_info(test_app, test_user):
    new_data = {'name': 'Updated Name', 'email': 'updated@example.com'}
    response = update_user_info(test_user.userid, new_data)
    assert response['message'] == 'User updated successfully'
    # Fetch the updated user and check the updated fields
    updated_user = User.query.get(test_user.userid)
    assert updated_user.name == 'Updated Name'
    assert updated_user.email == 'updated@example.com'
