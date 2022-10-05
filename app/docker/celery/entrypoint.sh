#!/bin/bash
set -e

sleep 10

exec celery -A djangoProject_own_group worker -l INFO

