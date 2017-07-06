class HexExistsError(Exception):
    def __init__(self, message):
        super(HexExistsError, self).__init__(message)


class IncorrectCoordinatesError(Exception):
    def __init__(self, message):
        super(IncorrectCoordinatesError, self).__init__(message)


class MismatchError(Exception):
    def __init__(self, message):
        super(MismatchError, self).__init__(message)
