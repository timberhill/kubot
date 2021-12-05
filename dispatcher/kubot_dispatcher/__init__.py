from .config import Config
from .dispatcher import Dispatcher
from .exceptions import (
    KubotDispatcherConfigError,
    KubotDispatcherError,
    KubotDispatcherRedditError
)

__all__ = [
    "Config",
    "Dispatcher",
    "KubotDispatcherError",
    "KubotDispatcherConfigError",
    "KubotDispatcherRedditError"
]

# get package version
from pathlib import Path
import re

pyproject_path = Path(__spec__.origin).parent.parent / "pyproject.toml"
with open(pyproject_path, "r") as pyproject_file:
    contents = pyproject_file.read()
    version_match = re.search(r"version = \"(?P<value>.+)\"\n", contents)
    __version__ = version_match.group(1)
