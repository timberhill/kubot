import asyncpraw
import asyncio


class Dispatcher:
    """
    Dispatcher class that streams data from Reddit API and
    sends it to the consumer bots.
    """
    def __init__(self, config, api_config) -> None:
        self.config = config
        self.reddit = asyncpraw.Reddit(**api_config)
        self.counter = 0

    def start(self) -> None:
        """Starts streaming reddit activity and sending it to the bots.
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.stream())

    async def stream(self) -> None:
        """Starts streaming reddit activity and sending it to the bots.
        """
        subreddit = await self.reddit.subreddit("all")
        async for submission in subreddit.stream.submissions():
            await self.process_submission(submission)

    async def process_submission(self, submission):
        self.counter += 1
        print(self.counter, submission)
