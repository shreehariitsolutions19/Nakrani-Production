
from pathlib import Path
import os

import dj_database_url
from dotenv import load_dotenv


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# ENVIRONMENT VARIABLES
# =========================================================

load_dotenv(BASE_DIR / ".env")


# =========================================================
# SECURITY SETTINGS
# =========================================================

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "change-me-in-production"
)

DEBUG = os.getenv(
    "DEBUG",
    "False"
).lower() == "true"


# =========================================================
# ALLOWED HOSTS
# =========================================================

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        "graphix-django-before.onrender.com,localhost,127.0.0.1"
    ).split(",")
    if host.strip()
]

if "nakrani-production.onrender.com" not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(
        "nakrani-production.onrender.com"
    )


# =========================================================
# CSRF TRUSTED ORIGINS
# =========================================================

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "CSRF_TRUSTED_ORIGINS",
        "https://graphix-django-before.onrender.com"
    ).split(",")
    if origin.strip()
]

if (
    "https://nakrani-production.onrender.com"
    not in CSRF_TRUSTED_ORIGINS
):
    CSRF_TRUSTED_ORIGINS.append(
        "https://nakrani-production.onrender.com"
    )


# =========================================================
# INSTALLED APPS
# =========================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "website",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# URL CONFIGURATION
# =========================================================

ROOT_URLCONF = "config.urls"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================================================
# WSGI APPLICATION
# =========================================================

WSGI_APPLICATION = "config.wsgi.application"


# =========================================================
# DATABASE CONFIGURATION
# =========================================================

DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_URL:

    # Render / External PostgreSQL Database

    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600
        )
    }

else:

    # Local PostgreSQL Database

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",

            "NAME": os.getenv(
                "POSTGRES_DB",
                "nakrani_production"
            ),

            "USER": os.getenv(
                "POSTGRES_USER",
                "postgres"
            ),

            "PASSWORD": os.getenv(
                "POSTGRES_PASSWORD",
                ""
            ),

            "HOST": os.getenv(
                "POSTGRES_HOST",
                "127.0.0.1"
            ),

            "PORT": os.getenv(
                "POSTGRES_PORT",
                "5800"
            ),

            "CONN_MAX_AGE": 600,
        }
    }


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = []


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "website" / "static"
]


# =========================================================
# STORAGE CONFIGURATION
# =========================================================

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage"
    },

    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage."
            "CompressedManifestStaticFilesStorage"
        )
    },
}


# =========================================================
# MEDIA FILES
# =========================================================

MEDIA_URL = os.getenv(
    "MEDIA_URL",
    "/media/"
)

MEDIA_ROOT = Path(
    os.getenv(
        "MEDIA_ROOT",
        str(BASE_DIR / "media")
    )
)


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)


# =========================================================
# GOOGLE FORM INTEGRATION
# =========================================================

GOOGLE_FORM_URL = os.getenv(
    "GOOGLE_FORM_URL",
    ""
)

GOOGLE_FORM_ENTRY_NAME = os.getenv(
    "GOOGLE_FORM_ENTRY_NAME",
    ""
)

GOOGLE_FORM_ENTRY_EMAIL = os.getenv(
    "GOOGLE_FORM_ENTRY_EMAIL",
    ""
)

GOOGLE_FORM_ENTRY_PHONE = os.getenv(
    "GOOGLE_FORM_ENTRY_PHONE",
    ""
)

GOOGLE_FORM_ENTRY_COMPANY = os.getenv(
    "GOOGLE_FORM_ENTRY_COMPANY",
    ""
)

GOOGLE_FORM_ENTRY_PROJECT_TYPE = os.getenv(
    "GOOGLE_FORM_ENTRY_PROJECT_TYPE",
    ""
)

GOOGLE_FORM_ENTRY_BUDGET = os.getenv(
    "GOOGLE_FORM_ENTRY_BUDGET",
    ""
)

GOOGLE_FORM_ENTRY_TIMELINE = os.getenv(
    "GOOGLE_FORM_ENTRY_TIMELINE",
    ""
)

GOOGLE_FORM_ENTRY_MESSAGE = os.getenv(
    "GOOGLE_FORM_ENTRY_MESSAGE",
    ""
)