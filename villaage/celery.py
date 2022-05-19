from __future__ import absolute_import

import os

from celery import Celery
from villaage.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "villaage.settings.development")

app = Celery("villaage")

app.config_from_object("villaage.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)