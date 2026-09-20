from .base import *

DEBUG = False

ADMINS = [
    ("Moses N", "moseswambui044@gmail.com")
]

ALLOWED_HOSTS = ["*",]
REDIS_URL = "redis://cache:6379"
CACHES["default"]["LOCATION"] = REDIS_URL
CHANNEL_LAYERS["default"]["config"]["hosts"] = [REDIS_URL]