"""Kubot Dispatcher exceptions"""


class KubotDispatcherError(Exception):
    """Generic Kubot Dispatcher exception

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


class KubotDispatcherConfigError(KubotDispatcherError):
    """Kubot Dispatcher exception related to Config

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message) -> None:
        self.message = f"Error parsing the config: {message}"
        super().__init__(self.message)


class KubotModelSerialiserError(KubotDispatcherError):
    """Kubot Model Serialiser exception

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message) -> None:
        self.message = f"Error serialising reddit object: {message}"
        super().__init__(self.message)
