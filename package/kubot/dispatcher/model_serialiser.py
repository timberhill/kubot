import json

from asyncpraw.models.reddit.submission import Submission
from asyncpraw.models.reddit.comment import Comment


class ModelSerialiser:
    """Routines to serialise AsyncPRAW models
    """
    def __init__(self, obj) -> None:
        self.obj = obj

    def to_dict(self, addon=dict()):
        """Return a json representation of the object as a dict
        """
        if isinstance(self.obj, Submission):
            return self._submission_to_dict(self.obj, addon)
        if isinstance(self.obj, Comment):
            return self._comment_to_dict(self.obj, addon)

    def to_json(self, addon=dict()):
        """Return a json representation of the object as a string
        """
        return json.dumps(self.to_dict(addon))

    def _submission_to_dict(self, obj: Submission, addon: dict):
        serialised_dict = obj.__dict__
        serialised_dict.pop("_reddit")
        serialised_dict.pop("comments")
        serialised_dict["subreddit"] = \
            serialised_dict["subreddit"].display_name
        serialised_dict["author"] = \
            serialised_dict["author"].name

        serialised_dict.update(addon)
        return serialised_dict

    def _comment_to_dict(self, obj: Comment, addon: dict):
        serialised_dict = obj.__dict__
        serialised_dict.pop("_reddit")
        serialised_dict["subreddit"] = \
            serialised_dict["subreddit"].display_name
        serialised_dict["author"] = \
            serialised_dict["author"].name

        serialised_dict.update(addon)
        return serialised_dict
