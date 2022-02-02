# ------- 3rd party imports -------
from flask_sqlalchemy import SQLAlchemy
import redis
import os

db = SQLAlchemy()
redis = redis.Redis(
  host=os.environ.get('REDIS_HOST'),
  port=os.environ.get('REDIS_PORT'),
  password=os.environ.get('REDIS_PASSWORD')
)
