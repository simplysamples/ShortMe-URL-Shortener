# ------- 3rd party imports -------
from flask_sqlalchemy import SQLAlchemy
import redis
import os

db = SQLAlchemy()
redis = redis.Redis(
  host=os.environ.get('ADMIN_USERNAME'),
  port=os.environ.get('ADMIN_PORT'),
  password=os.environ.get('ADMIN_PASSWORD')
)
