from kubot.client import KubotClient

from .comment_reader import CommentHandler
from .submission_reader import SubmissionHandler

client = KubotClient(SubmissionHandler, CommentHandler)
client.start()
