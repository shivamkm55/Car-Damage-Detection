

# Car Damage Detection

## Celery integration

This project now includes Celery integration for background tasks using Redis.

### Setup
- Install dependencies: `pip install -r requirements.txt`
- Start Redis locally (or update `REDIS_URL` / `CELERY_BROKER_URL`)
- Start a Celery worker:
  `celery -A celery_worker worker --loglevel=info`

### Example
Visit `/celery-test` in the Flask app to queue a sample background task.
