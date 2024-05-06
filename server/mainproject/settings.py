import os
from dotenv import load_dotenv, dotenv_values
import environ
from pathlib import Path
import pymysql.cursors
from django.template.context_processors import media

pymysql.version_info = (1, 4, 3, "final", 0)
pymysql.install_as_MySQLdb()


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv()
# Initialise environment variables
# env = environ.Env()
# environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "****************hidden*************************************"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = ["127.0.0.1", "*"]

# CSRF_TRUSTED_ORIGINS = [

# ]
# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "mainapp.apps.MainappConfig",
    # "cloudinary_storage",  # Refer to https://pypi.org/project/django-cloudinary-storage/ documentation
    # "cloudinary",
    "livereload",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_daraja",
    "django_otp",
    "django_otp.plugins.otp_totp",
]


CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUD_NAME"),
    "API_KEY": os.getenv("API_KEY"),
    "API_SECRET": os.getenv("API_SECRET"),
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "livereload.middleware.LiveReloadScript",
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "",
    }
}

ROOT_URLCONF = "mainproject.urls"
LOGIN_URL = "login"
LOGIN_REDIRECT = "login"
LOGIN_REDIRECT_URL = "dashboard"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "mainapp/templates"],
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

WSGI_APPLICATION = "mainproject.wsgi.application"

# The email backend to use. For possible shortcuts see django.core.mail.
# The default is to use the SMTP backend.
# Third-party backends can be specified by providing a Python path
# to a module that defines an EmailBackend class.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Host for sending email.
EMAIL_HOST = "smtp.gmail.com"
# Port for sending email.
EMAIL_PORT = 587
# Whether to send SMTP 'Date' header in the local time zone or in UTC.
EMAIL_USE_LOCALTIME = True
# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_TIMEOUT = None
DEFAULT_FROM_EMAIL = "Uninotes <noreply@projectsdjango.com>"

# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env('DATABASE_NAME'),
#         'USER': env('DATABASE_USER'),
#         'PASSWORD': env('DATABASE_PASS'),
#         'HOST': env('DATABASE_HOST'),
#         'PORT': env('DATABASE_PORT'),
#         "OPTIONS": {
#             "ssl": {"ssl-ca": env('SSL_CA')},
#             "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
#             "ssl_disabled": 0,
#         },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

STATIC_URL = "/static/"
STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"

# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

MEDIA_URL = "media/"

# DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.RawMediaCloudinaryStorage"

# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "mainapp/static")]

else:
    STATIC_ROOT = os.path.join(BASE_DIR, "mainapp/static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


MPESA_ENVIRONMENT = ""

# Credentials for the daraja app

MPESA_CONSUMER_KEY = ""
MPESA_CONSUMER_SECRET = ""

# Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

MPESA_SHORTCODE = ""

# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# This is only used on sandbox, do not set this variable in production
# For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page

MPESA_EXPRESS_SHORTCODE = ""

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)

MPESA_SHORTCODE_TYPE = ""

# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

MPESA_PASSKEY = ""

# Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_USERNAME = "testapi"

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_SECURITY_CREDENTIAL = ""
