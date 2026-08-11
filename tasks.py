from app import celery


@celery.task(name='tasks.add')
def add(x, y):
    """Simple example task that adds two numbers."""
    return x + y


@celery.task(name='tasks.long_task')
def long_task(seconds):
    import time
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"
