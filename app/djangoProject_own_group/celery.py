import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject_own_group.settings")

celery_app = Celery("djangoProject_own_group")

celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
