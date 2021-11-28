"""Test Config class functionality"""
import pytest

from src.config import Config

GOOD_CONFIG_PATH = "tests/config-examples/config_good_1.yaml"
BAD_CONFIG_PATH = "tests/config-examples/config_bad_1.yaml"


def validate_good_config(instance: Config) -> None:

    correct_subreddits = sorted(["dirt", "tidy", "neat"])
    correct_bot = "example-bot"
    assert (
        instance.bots.get(correct_bot, None) is not None
        and sorted(instance.bots.get(correct_bot).subreddits)
        == correct_subreddits
        and len(set(instance.bots.get(correct_bot).subreddits))
        == len(correct_subreddits)
    )


def test_init() -> None:
    """Test importing Config class"""
    from src import Config

    raw_config = {
        "subreddits": [
            {"name": "clean", "add": ["tidy", "neat"]},
            {"name": "dirty", "inherit": ["clean"], "add": ["dirt"]},
        ],
        "bots": [
            {
                "name": "example-bot",
                "subreddits": "dirty",
                "comments": "no",
                "submissions": "yes",
            }
        ],
    }

    config = Config(raw_config)
    validate_good_config(config)


def test_config_from_file() -> None:
    """Test the good config example is parsed correctly from file"""
    from src import Config
    config = Config.from_file(GOOD_CONFIG_PATH)
    validate_good_config(config)


def test_config_from_string() -> None:
    """Test the good config example is parsed correctly from string"""
    from src import Config

    with open(GOOD_CONFIG_PATH, "r") as good_config_file:
        good_config_string = good_config_file.read()

    config = Config.from_string(good_config_string)
    validate_good_config(config)


def test_config_cyclic_inheritance() -> None:
    """Test the bad example raises a correct exception for cyclic inheritance
    """
    from src import Config
    from src import KubotDispatcherError

    with pytest.raises(KubotDispatcherError):
        Config.from_file(BAD_CONFIG_PATH)
