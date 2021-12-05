import os

from .config import Config
from .dispatcher import Dispatcher
from . import __version__


try:
    config = Config.from_file("config-example.yaml")

    api_config = dict(
        client_id=os.environ.get("REDDIT_CLIENT_ID"),
        client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
        user_agent=f"python:{__package__}:{__version__} (by /u/timberhilly)",
        redirect_uri="http://localhost:8080"
    )

    Dispatcher(config, api_config).start()
except Exception as e:
    print(f"Critical error in __main__.py: {e}")
