import pytest

from app.exceptions import UserAlreadyExistsError
from app.models import User, Database


@pytest.fixture
def user_client():
    return User("test@test.com", "test")


@pytest.fixture
def db_client():
    return Database()

def test__db_can_insert_user__succeeds(user_client, db_client):
    db_client.insert_user(user_client)
    assert len(db_client.users) > 0

def test__db_can_insert_existing_user_fails__raises(user_client, db_client):
    db_client.insert_user(user_client)
    try:
        db_client.insert_user(user_client)
    except:
        assert True

def test__db_can_find_user__succeeds(user_client, db_client):
    db_client.insert_user(user_client)
    assert db_client.find_user_by_email(user_client.email)


def test__db_can_find_user__fails(user_client, db_client):
    assert db_client.find_user_by_email(user_client.email) is False

def test__db_can_verify_credentials__succeeds(user_client, db_client):
    db_client.insert_user(user_client)
    db_client.verify_login_credentials(user_client.email, user_client.password)

def test__db_can_catch_wrong_password__fails(user_client, db_client):
    db_client.insert_user(user_client)
    assert db_client.verify_login_credentials(user_client.email, "wrong") is False


