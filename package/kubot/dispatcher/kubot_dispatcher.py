import asyncpraw
import asyncio
import json
import socket
from datetime import datetime

from asyncpraw.models.reddit.submission import Submission
from asyncpraw.models.reddit.comment import Comment

from .kubot_dispatcher_config import KubotDispatcherConfig
from .model_serialiser import ModelSerialiser


class KubotDispatcher:
    """
    Dispatcher class that streams data from Reddit API and
    sends it to the consumer bots.
    """

    def __init__(self, config: KubotDispatcherConfig, api_config: dict):
        self.config = config
        self.reddit = asyncpraw.Reddit(**api_config)

    def start(self) -> None:
        """Starts streaming reddit activity and sending it to the bots.
        """
        print(self.config.comment_subreddits)

        loop = asyncio.get_event_loop()
        loop.create_task(self._stream_comments())
        loop.create_task(self._stream_submissions())
        loop.run_forever()

    async def _stream_submissions(self) -> None:
        """Stream submissions asynchronously. Calls self._dispatch_submission()
        """
        subreddit = await self.reddit.subreddit(
            "+".join(self.config.submission_subreddits))
        async for submission in subreddit.stream.submissions(pause_after=-1):
            if submission is None:
                continue
            await self._dispatch_submission(submission)

    async def _stream_comments(self) -> None:
        """Stream comments asynchronously. Calls self._dispatch_comment()
        """
        subreddit = await self.reddit.subreddit(
            "+".join(self.config.comment_subreddits))
        async for comment in subreddit.stream.comments(pause_after=-1):
            if comment is None:
                continue
            await self._dispatch_comment(comment)

    async def _dispatch_submission(self, submission: Submission) -> None:
        """Dispatch a submission.

        Args:
            submission (asyncpraw.models.reddit.submission.Submission):
                submission object to process
        """
        dispatch_time = datetime.utcnow().timestamp()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.connect(("localhost", 37998))
            json_string = ModelSerialiser(submission) \
                .to_json(addon=dict(dispatch_time=dispatch_time))
            sock.sendall(bytes(json.dumps(json_string) + "\n", "utf-8"))
            print(f"SENT SUBMISSION, status={str(sock.recv(10), 'utf-8')}")

    async def _dispatch_comment(self, comment: Comment) -> None:
        """Dispatch a comment.

        Args:
            comment (asyncpraw.models.reddit.comment.Comment):
                comment object to process
        """
        dispatch_time = datetime.utcnow().timestamp()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("localhost", 37999))
            json_string = ModelSerialiser(comment) \
                .to_json(addon=dict(dispatch_time=dispatch_time))
            sock.sendall(bytes(json.dumps(json_string) + "\n", "utf-8"))
            print(f"SENT COMMENT, status={str(sock.recv(10), 'utf-8')}")
