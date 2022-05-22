import pytest
from app import create_app, db

@pytest.fixture()
def app():
    app = create_app("testing")

    # other setup can go here
    app_context = app.app_context()
    app_context.push()

    db.create_all()

    yield app

    # clean up / reset resources here
    db.session.remove()
    db.drop_all()
    app_context.pop()

@pytest.fixture
def client(app):
    return app.test_client()