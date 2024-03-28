import os
from.settings import *
from.settings import BASE_DIR
ALLOWED_HOSTS=[os.environ['WEBSITE_HOSTNAME']]
CSR_TRUSTED_ORIGINS =["https://"+os.environ['WEBSITE_HOSTNAME']]
DEBUG=False
SECRET_KEY = os.environ["MY_SECRET_KEY"]
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
# CORS_ALLOWED_ORIGIND=[

# ]

STORAGES = {

    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
CONNECTION=os.environ('azuar_postagral_sql')
CONNECTION_STR={pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CONNECTION_STR['dbname'],
         "HOST": CONNECTION_STR['host'],
        "USER":CONNECTION_STR['user'],
        "PASSWORD": CONNECTION_STR['password'],
       
        "PORT": "5432",
    }
}
STATIC_ROOT=BASE_DIR/'staticfiles'