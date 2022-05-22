from app.models.user import User
from app import db

import json

def test_user_get(client):
    """ Test getting a user from DB """

    # Create a mock user
    username = "test1234"
    user = User(username=username)

    db.session.add(user)
    db.session.commit()

    user_resp = client.get("api/v1/user/test1234")
    user_data = json.loads(user_resp.data.decode())

    assert user_resp.status_code == 200

    