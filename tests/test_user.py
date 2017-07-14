import pytest

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

def test__user_can_create_bucket__succeeds(user_client):
    user_client.create_bucket_list(bucket_name="Bucky",
                                   description="Descr")
    assert len(user_client.buckets) > 0

def test__user_can_delete_bucket__succeeds(user_client):
    user_client.create_bucket_list(bucket_name="Bucky",
                                   description="Descr")
    user_client.delete_bucket("Bucky")
    assert len(user_client.buckets) == 0

def test__user_can_find_bucket__succeeds(user_client):
    user_client.create_bucket_list(bucket_name="Bucky",
                                   description="Descr")
    bucket = user_client.find_bucket("Bucky")
    assert bucket is not None
