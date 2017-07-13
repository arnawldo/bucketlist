import unittest
from bucketlist.applicationmanager import ApplicationManager
from bucketlist.models import User

class Test(unittest.TestCase):
    def setUp(self):
        self.app = Database()
        email = ""
        password = ""
        self.user = self.app.create_user(first_name, last_name, email, password)