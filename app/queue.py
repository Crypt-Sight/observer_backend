from celery import Celery
from app.config import config

tasks = []

celery = Celery(
    "observer_backend",
    broker=config.amqp_dsn.unicode_string(),
    include=tasks
)

celery.conf.worker_pool_restarts = True
celery.conf.broker_connection_retry_on_startup = True
