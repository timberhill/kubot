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
        loop.run_until_complete(self._stream_submissions())

    async def _stream_submissions(self) -> None:
        """Stream submissions asynchronously. Calls self._process_submission()
        """
        subreddit = await self.reddit.subreddit("memes+gaming")
        async for submission in subreddit.stream.submissions():
            await self._process_submission(submission)

    async def _process_submission(self, submission) -> None:
        """Process a submission.

        Args:
            submission (asyncpraw.models.reddit.submission.Submission):
                submission object to process
        """
        self.counter += 1
        print(self.counter, submission.title)
