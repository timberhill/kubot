import jsonschema
import os
import yaml
from dataclasses import dataclass
from typing import Tuple

from .exceptions import KubotDispatcherConfigError


class Config:
    """Read config file, validate and act as a convenient container."""

    def __init__(self, raw: dict) -> None:
        self._raw = raw
        self._validate()
        self._gather_bot_data()

    @classmethod
    def from_string(self, config_string: str):
        raw = yaml.load(config_string, Loader=yaml.BaseLoader)
        return Config(raw)

    @classmethod
    def from_file(self, config_path: str):
        with open(config_path, "r") as config_file:
            raw = yaml.load(config_file, Loader=yaml.BaseLoader)
        return Config(raw)

    @property
    def comment_subreddits(self) -> list:
        """List of subreddits to fetch comments from.
        All bots/lists are combined here.

        Returns:
            list: subreddits
        """
        return list(
            set(
                subreddit
                for botconfig in self.bots.values()
                if botconfig.comments
                for subreddit in botconfig.subreddits
            )
        )

    @property
    def submission_subreddits(self) -> list:
        """List of subreddits to fetch submissions from.
        All bots/lists are combined here.

        Returns:
            list: subreddits
        """
        return list(
            set(
                subreddit
                for botconfig in self.bots.values()
                if botconfig.submissions
                for subreddit in botconfig.subreddits
            )
        )

    def _validate(self) -> None:
        schema_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "config-schema.yaml"
        )
        with open(schema_path, "r") as schema_file:
            schema = yaml.load(schema_file, Loader=yaml.BaseLoader)
            jsonschema.validate(self._raw, schema)

    def _gather_bot_data(self) -> None:
        """Handle subreddit inheritance and set class properties"""

        def _gather_subreddit_list(
            lists: list, list_name: str, history: list
        ) -> Tuple[list, list]:
            """Gather all subreddits in a list recursively based on inheritance.

            Args:
                lists (list): list of subreddits in a raw config structure
                list_name (str): name of the subreddit list
                history (list): list of subreddit lists already resolved
                    to avoid cyclic inheritance

            Raises:
                KubotDispatcherConfigError: cyclic inheritance detected
                KubotDispatcherConfigError: name not found

            Returns:
                Tuple[list, list]: history, list of subreddits in 'list_name'
            """
            # get the element for this subreddit list
            subreddit_data = next(
                (item for item in lists if item.get("name") == list_name), None
            )
            if subreddit_data is None:
                raise KubotDispatcherConfigError(
                    f"Couldn't find subreddit list named '{list_name}'"
                )

            # make sure that the recursion is not cyclic
            if list_name in history \
                    or list_name in subreddit_data.get("inherit", []):
                raise KubotDispatcherConfigError(
                    "Encountered cyclic inheritance in the subreddit lists"
                )

            # list of subreddit names to add to the current list
            add_subreddits = subreddit_data.get("add", [])

            # list of subreddit names to inherit from another lists
            history.append(list_name)
            for inherit_name in subreddit_data.get("inherit", []):
                history, inherited_subreddits = _gather_subreddit_list(
                    lists, inherit_name, history
                )
                add_subreddits.extend(inherited_subreddits)

            # add current subreddit list name to the history
            return history, add_subreddits

        # get full list of bots
        self.bots = dict()
        for bot in self._raw.get("bots"):
            _, subreddit_list = _gather_subreddit_list(
                self._raw.get("subreddits"), bot.get("subreddits"), []
            )

            include_submissions = \
                True if bot.get("submissions", "yes") == "yes" else False
            include_comments = \
                True if bot.get("comments", "yes") == "yes" else False

            self.bots[bot.get("name")] = BotConfig(
                name=bot.get("name"),
                subreddits=subreddit_list,
                submissions=include_submissions,
                comments=include_comments,
            )


@dataclass
class BotConfig:
    """Container class for a bot config"""

    name: str
    subreddits: list
    comments: bool
    submissions: bool
