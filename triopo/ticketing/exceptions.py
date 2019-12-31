class ContradictoryUserDetailsException(Exception):
    def __init__(self):
        self.message = (
            'User details do not match - are all of the details you are '
            'passing in for the same user?'
        )


class NotEnoughInfoException(Exception):
    pass


class TooMuchInfoException(Exception):
    """Hahaha"""
    pass
