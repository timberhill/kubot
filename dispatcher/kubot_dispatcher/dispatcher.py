import praw


class Dispatcher:
    """
    Dispatcher class that streams data from Reddit API and
    sends it to the consumer bots.
    """
    def __init__(self, config, api_config) -> None:
        self.config = config
        self.reddit = praw.Reddit(**api_config)

    def start(self) -> None:
        pass
