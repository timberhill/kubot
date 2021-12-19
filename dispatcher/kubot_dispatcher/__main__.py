import os
from kubot.dispatcher import KubotDispatcherConfig, KubotDispatcher

__version__ = "0.1.1"


try:
    config = KubotDispatcherConfig.from_file("config-example.yaml")

    api_config = dict(
        client_id=os.environ.get("REDDIT_CLIENT_ID"),
        client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
        user_agent=f"python:{__package__}:{__version__} (by /u/timberhilly)",
        redirect_uri="http://localhost:8080"
    )

    KubotDispatcher(config, api_config).start()
except Exception as e:
    print(f"Critical error in __main__.py: {e}")
