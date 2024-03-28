import os
from .settings import *

# Set ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS
ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME', '')]
CSRF_TRUSTED_ORIGINS = ["https://" + os.environ.get('WEBSITE_HOSTNAME', '')]

# Debug should be False in production
DEBUG = False

# Load SECRET_KEY from environment variable
SECRET_KEY = os.environ.get("MY_SECRET_KEY")

# Define middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Define database connection
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get('MYSQL_DATABASE'),
        "HOST": os.environ.get('MYSQL_HOST'),
        "USER": os.environ.get('MYSQL_USER'),
        "PASSWORD": os.environ.get('MYSQL_PASSWORD'),
        "PORT": os.environ.get('MYSQL_PORT', '3306'),
    }
}

# Define static root
STATIC_ROOT = BASE_DIR / 'staticfiles'
