from djangoProject_own_group.celery import celery_app
import time


@celery_app.task()
def add_method(x: int, y: int) -> int:
    print('=== TASK === STARTED !!! ===')
    time.sleep(11)
    print('=== TASK === ENDED !!! ===')
    return x + y
