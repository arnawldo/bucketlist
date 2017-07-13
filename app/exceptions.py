class BucketListAppErrors(Exception):
    """Base class for application errors"""

    def __init__(self, message):
        self.message = message

class UserAlreadyExistsError(Exception):
    pass

class BucketListAlreadyExistsError(Exception):
    pass


class UserError(Exception):
    pass


class UserNotExistsError(Exception):
    pass


class IncorrectPasswordError(Exception):
    pass


class UserAlreadyRegisteredError(Exception):
    pass


class InvalidEmailError(Exception):
    pass

class ValidationError(ValueError):
    pass