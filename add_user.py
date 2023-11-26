from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    user_to_delete = db.session.get(User, 1)
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
    new_user = User(userid=1, name='exampleName', email='exampleEmail@example.com', profile_picture='photo_url_1')
    db.session.add(new_user)
    db.session.commit()
