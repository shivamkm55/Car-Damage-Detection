import os
from celery import Celery


def make_celery(flask_app):
    """Create and configure a Celery object using Flask app config."""
    broker = flask_app.config.get(
        "CELERY_BROKER_URL",
        os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    )
    backend = flask_app.config.get(
        "CELERY_RESULT_BACKEND",
        os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1"),
    )

    celery_app = Celery(
        flask_app.import_name,
        broker=broker,
        backend=backend,
        include=["tasks"],
    )

    celery_app.conf.update(flask_app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app
