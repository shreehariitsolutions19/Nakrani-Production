#!/usr/bin/env bash
set -o errexit

python -m pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

if [ -n "${DJANGO_ADMIN_USERNAME:-}" ] && [ -n "${DJANGO_ADMIN_PASSWORD:-}" ]; then
	python manage.py shell <<'PY'
import os

from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ["DJANGO_ADMIN_USERNAME"]
user, _ = User.objects.get_or_create(username=username)
user.email = os.getenv("DJANGO_ADMIN_EMAIL", "")
user.is_staff = True
user.is_superuser = True
user.set_password(os.environ["DJANGO_ADMIN_PASSWORD"])
user.save()
PY
fi