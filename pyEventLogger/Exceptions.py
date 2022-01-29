"""
The Exceptions File
"""


class LogOptionException(Exception):
    """
    Raised when a Log option such as print_log and make_file is invalid or False
    """
    pass


class LogTypeException(Exception):
    """
    Raised when a Log type is invalid
    """
    pass
