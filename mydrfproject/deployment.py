import os
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSR_TRUSTED_ORIGINS = ["https://" + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False
SECRET_KEY = os.environ["MY_SECRETE_key"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

CONNECTION = os.environ['AZURE_MYSQL_CONNECTION_STRING']
CONNECTION_STR = {pair.split('=')[0]: pair.split('=')[1] for pair in CONNECTION.split(';')}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": CONNECTION_STR['Database'],
        "HOST": CONNECTION_STR['Server'],
        "USER": CONNECTION_STR['User Id'],
        "PASSWORD": CONNECTION_STR['Password'],
        "PORT": CONNECTION_STR.get('Port', '3306'),  # Assuming default port is 3306
        "OPTIONS": {'charset': 'utf8mb4'},  # If you're using utf8mb4 charset
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
