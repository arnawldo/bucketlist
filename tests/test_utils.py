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