import os
import kubot

__version__ = "0.1.1"


try:
    config = kubot.Config.from_file("config-example.yaml")

    api_config = dict(
        client_id=os.environ.get("REDDIT_CLIENT_ID"),
        client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
        user_agent=f"python:{__package__}:{__version__} (by /u/timberhilly)",
        redirect_uri="http://localhost:8080"
    )

    kubot.Dispatcher(config, api_config).start()
except Exception as e:
    print(f"Critical error in __main__.py: {e}")
