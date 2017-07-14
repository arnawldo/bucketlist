
import re

from app.exceptions import UserNotExistsError, IncorrectPasswordError, UserAlreadyExistsError


class Database(object):
    """Class for temporary storage of instances of User, BucketList, and Task"""

    def __init__(self):

        # store for users, bucket lists, and tasks
        self.users = []


    def insert_user(self, user):
        """
        Insert user instance into database

        :param user: User instance
        :type user: User
        :return: True if successful, False otherwise
        :rtype: bool
        """
        # check if similar user already exists
        for db_user in self.users:
            if user.email == db_user.email:
                raise UserAlreadyExistsError("User already exists!")
        # register user
        self.users.append(user)
        return True

    def find_user_by_email(self, email):
        """
        Searches for a user by given email

        :param email: Email of user
        :type attr: str
        :return: User instance with given email, else None if not found
        """
        for user in self.users:
            if user.email == email:
                return user

        # user not found
        return False

    def verify_login_credentials(self, email, password):
        """
        Verify if email and password entered by user are authentic

        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """

        user = self.find_user_by_email(email)

        if user:
            if user.password == password:
                return True
            return False
        # no user was found
        raise UserNotExistsError



class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: The sha512 password from the login/register form
        :return: A sha512->pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password the user sent matches that of the database.
        The database password is encrypted more than the user's password at this stage.
        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True if passwords match, False otherwise
        """
        return pbkdf2_sha512.verify(password, hashed_password)


class BucketList(object):
    """Class of user bucket lists"""

    def __init__(self, bucket_name, description=None):
        """
        Instantiate BucketList object

        :param bucket_name: Name of the bucket list
        :type bucket_name: str
        :param description: optional description of bucket list
        :type description: str
        """
        self.bucket_name = bucket_name
        self.description = description
        self.tasks = [] # store for to-do tasks

    def create_task(self, description, due_date=None):
        """
        Create new task

        :param description: Description of task
        :param due_date: Optional due date of task
        :return: None
        """
        task = Task(description, due_date)
        # save to bucket list
        self.tasks.append(task)


    def __repr__(self):
        return "<BueckList {bucket_name} \nby: {username} >".format(name=self.bucket_name, username=self.username)

class Task(object):
    """Class for bucket list tasks"""

    def __init__(self, description, due_date=None):
        """
        Instantiate task object

        :param description: Description of task
        :param due_date: optional due date
        """
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return "<Task: {description}>".format(description=self.description)

class User(object):
    """Class for the app users"""

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.buckets = []

    # username, bucket_name, description=None
    def create_bucket_list(self, bucket_name, description=None):
        """
        Create a bucket list

        :param bucket_name: Name of bucket list to be created
        :param description: Description of bucket list
        :return: True if bucket list was successfully created, False otherwise
        """
        bucket = BucketList(bucket_name, description)
        self.buckets.append(bucket)

    def delete_bucket(self, bucket_name):
        """
        Delete a bucket list

        :param bucket_name: Name of bucket list to be deleted
        :return: True if bucket list was successfully deleted, False otherwise
        """
        pos = None
        for i, bucket in enumerate(self.buckets):
            if bucket.bucket_name == bucket_name:
                pos = i
        if pos is not None:
            del self.buckets[pos]
            return True
        else:
            return False

    def find_bucket(self, bucket_name):
        """
        Find bucket by name

        :param bucket_name: Name of bucket list to be found
        :return: BucketList if found, False otherwise
        """
        pos = None
        for i, bucket in enumerate(self.buckets):
            if bucket.bucket_name == bucket_name:
                pos = i
        if pos is not None:
            return self.buckets[pos]






    def __repr__(self):
        return "<User {}>".format(self.username)