from .config import Config
from .dispatcher import Dispatcher
from . import __version__


config = Config.from_file("config-example.yaml")
api_config = dict(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="PASSWORD",
    user_agent=f"python:{__package__}:{__version__}",
    username="USERNAME",
)

print(api_config)

dispatcher = Dispatcher(config, api_config)
