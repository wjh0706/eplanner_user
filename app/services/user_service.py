from ..models.user import User
from .. import db

def get_user_info(userid):
    """
    Retrieves user information based on the user ID.
    """
    user = db.session.get(User, userid)
    if user:
        return {
            "userid": user.userid,
            "name": user.name,
            "email": user.email,
            "profile_picture": user.profile_picture
        }
    else:
        return {"error": "User not found"}, 404

def update_user_info(userid, data):
    """
    Updates user information given the user ID and new data.
    """
    user = db.session.get(User, userid)
    if user:
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        # Add additional fields here as necessary

        db.session.commit()
        return {"message": "User updated successfully"}
    else:
        return {"error": "User not found"}, 404

def update_user_photo(userid, data):
    """
    Updates the profile picture of the user.
    """
    user = db.session.get(User, userid)
    if user:
        user.profile_picture = data.get('profile_picture', user.profile_picture)
        db.session.commit()
        return {"message": "Profile photo updated successfully"}
    else:
        return {"error": "User not found"}, 404
