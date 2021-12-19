"""Test Config class functionality"""
import pytest

from kubot.config import Config

GOOD_CONFIG_PATH = "tests/config-examples/config_good_1.yaml"
BAD_CONFIG_PATH = "tests/config-examples/config_bad_1.yaml"

example_bot = "example-bot-1"
example_bot_subreddits = sorted(["dirt", "tidy", "neat"])


def validate_good_config(instance: Config) -> None:
    """Validate the the config is correct according to the test file.

    Args:
        instance (Config): Config instance to be tested
    """
    assert instance.bots.get(example_bot, None) is not None
    assert sorted(set(instance.bots.get(example_bot).subreddits)) \
        == example_bot_subreddits
    assert len(set(instance.bots.get(example_bot).subreddits)) \
        == len(example_bot_subreddits)


def test_init() -> None:
    """Test importing Config class"""
    from kubot import Config

    raw_config = {
        "subreddits": [
            {"name": "clean", "add": ["tidy", "neat"]},
            {"name": "dirty", "inherit": ["clean"], "add": ["dirt"]},
        ],
        "bots": [
            {
                "name": "example-bot-1",
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
    from kubot import Config
    config = Config.from_file(GOOD_CONFIG_PATH)
    validate_good_config(config)


def test_config_from_string() -> None:
    """Test the good config example is parsed correctly from string"""
    from kubot import Config

    with open(GOOD_CONFIG_PATH, "r") as good_config_file:
        good_config_string = good_config_file.read()

    config = Config.from_string(good_config_string)
    validate_good_config(config)


def test_config_cyclic_inheritance() -> None:
    """Test the bad example raises a correct exception for cyclic inheritance
    """
    from kubot import Config
    from kubot import KubotDispatcherError

    with pytest.raises(KubotDispatcherError):
        Config.from_file(BAD_CONFIG_PATH)


def test_config_comment_subreddits() -> None:
    """Test comment_subreddits property
    """
    from kubot import Config
    config = Config.from_file(GOOD_CONFIG_PATH)
    assert isinstance(config.comment_subreddits, list) \
        and len(config.comment_subreddits) == len(example_bot_subreddits)


def test_config_submision_subreddits() -> None:
    """Test submision_subreddits property
    """
    from kubot import Config
    config = Config.from_file(GOOD_CONFIG_PATH)
    assert isinstance(config.submission_subreddits, list) \
        and len(config.submission_subreddits) == len(example_bot_subreddits)