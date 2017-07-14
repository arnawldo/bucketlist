import pytest

from app import create_app
from app.models import User, Database


@pytest.fixture
def user_client():
    return User("test@test.com", "test")


@pytest.fixture
def db_client():
    return Database()

def test__user_can_register__succeeds(user_client, db_client):
    db_client.insert_user(user_client)
    assert len(db_client.users) > 0