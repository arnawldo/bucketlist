import pytest

from app.models import BucketList, Task


@pytest.fixture
def bucket():
    return BucketList("Test bucket", "describe bucket")


def test__bucket_can_create_task__succeeds(bucket):
    bucket.create_task("Description of task")
    assert len(bucket.tasks) > 0
