import pytest

from app.models import Utils

@pytest.mark.parametrize("input_email, expected_output",[
    ("arnold@andela.com", True),
    ("arnold@andela", False),
    ("@andela", False),
    ("andela.com", False),
    ("arnold@andela.co.ug", True)
])
def test__util_can_validate_email__succeeds(input_email, expected_output):
    assert Utils.email_is_valid(input_email) is expected_output

def test__password_hashing__succeeds():
    password = "password"
    hashed = Utils.hash_password(password)
    assert password != hashed
    check_hashed = Utils.check_hashed_password(password, hashed)
    assert check_hashed
    wrong_password = "wrong"
    check_hashed = Utils.check_hashed_password(wrong_password, hashed)
    assert check_hashed is False