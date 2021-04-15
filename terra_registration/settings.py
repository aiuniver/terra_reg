"""
Django settings for terra_registration project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import environ
from envparse import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = environ.Path(__file__) - 2
env.read_envfile(BASE_DIR("terra_registration/.env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET")


# COLAB data
COLAB_DEBUG = env("COLAB_DEBUG")
COLAB_ALLOWED_HOST = env("COLAB_ALLOWED_HOST")
COLAB_API_URL = env("COLAB_API_URL")
COLAB_TUNNEL_USER = env("COLAB_TUNNEL_USER")
COLAB_RSA_KEY_FILE = env("COLAB_RSA_KEY_FILE")

COLAB_RSA_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAu+GU0vzimYAw8Idtkx88LYRL/Ev3JPOZ2d0666xIf+28pNLX
oG43vEig2ISl+vlVVylqLctsmFEQQQExaAxgMvEnoiXQ/gMdVuyw7lunohW6KIg5
hx2wsbkOcDfuS7XvoXcxTfMUHytOoiotLjXOOsW1ZuK92J7Va39M2qaM5Uyv/CR+
b/Uit1M44TCPv9QTw4A/Nl58hBi251ljvRrYwvseavZ+E++w6U1e1VZcmouHS3bG
Z45E1XydbFM1zLXUy5q7dnJgYLAThzNwX6ZFtpj/XNbbKY6zE5CFR/ImuhgEEbuw
gn3ExcRcImu5062bQSh0jzaqyLI3SYh0TMx1gwIDAQABAoIBABNkGOQdzZViMarh
j2Gb264m9WC4xm095ychOi+QvHrXopywVijstzvrkw5FwovAqBoy4A6R7EdcNn0/
DkZa4KLhWOHXXVaaI7ERBMHVG9wSuf/s72MOoWn2W5MhcqrFwFG954zQBcehxJ/g
EoGuc/aE6VARHt74pbZOkTQP9ILF1gvxQNSDNu8RGLmpAH7hd9z2gUbltG0aJ2SG
/m4D5k/w5H0EjpBcUiIpN7PrGk2rabWw9jfMa5aJDd4nIkZJTygoouiP0JG6XCpy
8eCiDh6hkssOkmsVUgIEptanHhCyR+8axPWr9tKxMrxk1bNU7eps/reJWD4X7c6K
qVuvycECgYEA7Pw+v4dfadciaJ2jOdTXnDWhhDploCSgj6CSv+pN4iHM+MXwQ+GO
770+6JxY2Ru2iTl4oztux5qHRIickh0MlBvO1GPeti2ttx5NCHTzzR1x2H5/GPly
p9YKH/c45TmYrA0jcp0X255Yd2romvXAYrsqSf26aAtUPN8arXQUcKsCgYEAyvS4
mjSUrvL2O8wxDsTpvgKAezI1Snp4b/5SQr6T4Ihh5/TrJPeuUrcOiuuGImznLsam
ozgiY4iY1TXhUKu9ortPWB2Gc307D3kh48UA8CuO84YH65sm5xVOWWHBtN4xzvUz
t3IBEQU04omBhwRHtGJ1HYdXBvZIfBAuzWs4fokCgYEAr/fRQ/hqAbYsJ5A9vlhr
zOMJzpxqD5KC4oMx1G1PbYT5pROdB1p5/0v/ZUuKsZNhY92X1WTxKid1H49s6xXE
3EkVuCF8IrwiTGGkg44L5hdiDIZJK6s11qgZFolE5vhwg/ixhI5fQ8T9HZb1pvKp
6uXdTdmoS092OkjTj04tS0cCgYB2qrYRO/M/g8HjXtXES/Bbb/0Ni2LLZGZtHSed
7O5r13JffL3MhKFBrdTr9yAbms9lczNVtemtht3NtE5Eq9Yagyi2XbUSa8OPnYTq
N3L/+of/7XtOEA6kCLoh2t220kAPQSF2/kqPWBr+5eV9O0xttS/DDzIcWP4yxAeJ
hkqm+QKBgQDdyhtcvSYXyUBc0lxhiaUnQLM965A2PGtOuh92sRJP/9fmKrhGiBuB
3R163d3iCOptvY7jwfZuJcwe3yMET+c02+DPTgjnL9/cSrPcwxz44cwpMz5T13Vx
mggeOqobZenJcV00gsvNpZHoXgjm3Z+yA5pLfOwWyg+Nma1HIqHIZQ==
-----END RSA PRIVATE KEY-----"""

ENVFILE_PATTERN = """SECRET_KEY={secret_key}
DEBUG={debug}
ALLOWED_HOSTS={allowed_hosts}
TERRA_AI_EXCHANGE_API_URL={api_url}
"""

MAKEFILE_PATTERN = """PORT={port}
TUNNEL_USER={tunnel_user}
RSA_KEY={rsa_key}
PREFIX={prefix}

run:
	echo "Makefile TerraGUI"

runserver:
	pip install -r /content/terra_gui/requirements/colab.txt
	chmod 400 /content/terra_gui/$(RSA_KEY)
	python /content/terra_gui/manage.py runserver 80 & ssh -i '/content/terra_gui/$(RSA_KEY)' -o StrictHostKeyChecking=no -R $(PORT):localhost:80 $(TUNNEL_USER)
	echo http://$(PREFIX).terra.neural-university.ru/project/datasets/
"""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "crispy_forms",
    "users",
]

if DEBUG:
    try:
        import debug_toolbar

        INSTALLED_APPS.append("debug_toolbar")
        DEBUG_TOOLBAR_CONFIG = {
            "SHOW_TOOLBAR_CALLBACK": lambda x: True,
            "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
            "SHOW_TEMPLATE_CONTEXT": True,
            "RESULTS_CACHE_SIZE": 100,
        }
    except ModuleNotFoundError:
        pass

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if "debug_toolbar" in INSTALLED_APPS:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

ROOT_URLCONF = "terra_registration.urls"

CRISPY_TEMPLATE_PACK = "bootstrap4"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "terra_registration.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR("db.sqlite3"),
    }
}

AUTH_USER_MODEL = "users.TerraUser"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR("staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_ext"),)

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = 'tmp/email-messages/'
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
EMAIL_HOST_USER = env("EMAIL_ADDRESS")
EMAIL_PORT = 465
EMAIL_USE_SSL = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
