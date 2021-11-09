# ------- 3rd party imports -------
from flask_sqlalchemy import SQLAlchemy
import redis
import app.app as a

db = SQLAlchemy()
redis = redis.Redis(
  host=a.REDIS_HOST,
  port=a.REDIS_PORT,
  password=a.REDIS_PASSWORD
)
