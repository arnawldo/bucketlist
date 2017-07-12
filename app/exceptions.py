class BucketListAppErrors(Exception):
    """Base class for application errors"""

    def __init__(self, message):
        self.message = message

class UserAlreadyExistsError(BucketListAppErrors):
    pass

class BucketListAlreadyExistsError(BucketListAppErrors):
    pass


class UserError(BucketListAppErrors):
    pass


class UserNotExistsError(UserError):
    pass


class IncorrectPasswordError(UserError):
    pass


class UserAlreadyRegisteredError(UserError):
    pass


class InvalidEmailError(UserError):
    pass

class ValidationError(ValueError):
    pass