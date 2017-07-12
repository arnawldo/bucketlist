from src.exceptions import UserAlreadyExistsError, BucketListAlreadyExistsError
from passlib.hash import pbkdf2_sha512
from src.exceptions import UserNotExistsError, IncorrectPasswordError
import re


class Database(object):
    """Class for temporary storage of instances of User, BucketList, and Task"""

    # store for users, bucket lists, and tasks
    users = []
    bucket_lists = []
    tasks= []


    @staticmethod
    def insert_user(user):
        """
        Insert user instance into database

        :param user: User instance
        :type user: User
        :return: True if successful, False otherwise
        :rtype: bool
        """
        # check if similar user already exists
        for db_user in Database.users:
            if user.username == db_user.username or user.email == db_user.email:
                raise UserAlreadyExistsError("User already exists!")
        # register user
        Database.users.append(user)
        return True

    @staticmethod
    def find_user_by_email(email):
        """
        Searches for a user by given email

        :param email: Email of user
        :type attr: str
        :return: User instance with given email, else None if not found
        """
        for user in Database.users:
            if user.email == email:
                return user

        # user not found
        return None


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

    def __init__(self, username, bucket_name, description=None):
        """
        Instantiate BucketList object

        :param username: Username of bucket owner
        :type username: str
        :param bucket_name: Name of the bucket list
        :type bucket_name: str
        :param description: optional description of bucket list
        :type description: str
        """
        self.username = username
        self.bucket_name = bucket_name
        self.description = description
        self.tasks = [] # store for to-do tasks

    def create_task(self, title, description, due_date=None):
        """
        Create new task

        :param title: Title of the task
        :param description: Description of task
        :param due_date: Optional due date of task
        :return: None
        """
        task = Task(self.bucket_name, title, description, due_date)
        # save to bucket list
        self.tasks.append(task)


    def __repr__(self):
        return "<BueckList {bucket_name} \nby: {username} >".format(name=self.bucket_name, username=self.username)

class Task(object):
    """Class for bucket list tasks"""

    def __init__(self, bucket_name, title, description, due_date=None):
        """
        Instantiate task object

        :param bucket_name: Name of bucket list that the task belongs to
        :param title: Title of task
        :param description: Description of task
        :param due_date: optional due date
        """
        self.bucket_name = bucket_name
        self.title = title
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return "<Task: {title} \nfrom: {bucket_name}>".format(title=self.title, bucket_name=self.bucket_name)

class User(object):
    """Class for the app users"""

    def __init__(self, username, email, password):
        self.username = username
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
        bucket = BucketList(self.username, bucket_name, description)
        self.buckets.append(bucket)


    @staticmethod
    def verify_login_credentials(username_or_email, password):
        """
        Verify if username/email and password entered by user are authentic

        :param username_or_email: The user's username or email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """
        # regular expression for matching emails
        email_regex_matcher = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if email_regex_matcher.match(username_or_email):
            # find user by email
            user = Database.find_user(attr=username_or_email, by="email")
        else:
            # find user by username
            user = Database.find_user(attr=username_or_email, by="username")
        if user is None:
            # no user was found
            raise UserNotExistsError
        elif Utils.check_hashed_password(password=password, hashed_password=user.password):
            raise IncorrectPasswordError

        return True


    def __repr__(self):
        return "<User {}>".format(self.username)