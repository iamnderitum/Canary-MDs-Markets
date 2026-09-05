ALLOWED_HOSTS = ("*",)
REDIS_URL = "redis://cache:6379"
CACHES["default"]["LOCATION"] = REDIS_URL
CHANNEL_LAYERS["default"]["config"]["hosts"] = [REDIS_URL]