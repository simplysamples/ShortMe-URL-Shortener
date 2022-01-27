# ------- 3rd party imports -------
from flask_sqlalchemy import SQLAlchemy
import redis
import os

db = SQLAlchemy()
redis = redis.Redis(
  host=os.environ.get('QOVERY_REDIS_ZBE8933FF_HOST'),
  port=os.environ.get('QOVERY_REDIS_ZBE8933FF_PORT'),
  password=os.environ.get('QOVERY_REDIS_ZBE8933FF_PASSWORD')
)
