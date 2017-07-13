import pytest
from flask import url_for

from app import create_app


@pytest.fixture
def app():
    app = create_app("default")
    return app

@pytest.fixture
def test_client(app):
    return app.test_client()


def test_app(client):
    assert True