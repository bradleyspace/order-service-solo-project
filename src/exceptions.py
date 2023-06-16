class DuplicateItemError(Exception):

    def __init__(self, message="Duplicate item added"):
        super().__init__(message)