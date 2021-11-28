from .config import Config

config = Config.from_file("config-example.yaml")
print(config.bots)
