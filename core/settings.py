"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv('.env.local')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# URL used to access the media from the front. Commentate this when populating doing scripts.
# MEDIA_URL = '/assets/ '

# Actual directory user files go to
# MEDIA_ROOT = os.path.join(os.path.basename(BASE_DIR), 'assets')
# MEDIA_ROOT = 'assets'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-izd-s4y1)vgjcf4vl%+&+n*65gvd0(ks%j%#ag6i(8azyf-i@#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', 'guardians-api-dev.us-west-2.elasticbeanstalk.com']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Adjust this to the actual origin of your frontend
    "http://127.0.0.1:3000"
]

# ALLOWED_HOSTS = ['*']
# CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication.apps.AuthenticationConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  # add if you want social authentication
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'corsheaders',
    'heroes',
    'villains',
    'django_extensions',
    'django_filters',
]

SITE_ID = 1  # make sure SITE_ID is set

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ----------------- email settings -----------------
import os

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"The {var_name} environment variable is not set"
        raise EnvironmentError(error_msg)

EMAIL_BACKEND = get_env_variable("EMAIL_BACKEND")
EMAIL_HOST = get_env_variable("EMAIL_HOST")
EMAIL_USE_TLS = get_env_variable("EMAIL_USE_TLS") == "True"
EMAIL_PORT = get_env_variable("EMAIL_PORT")
EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = get_env_variable("DEFAULT_FROM_EMAIL")
ACCOUNT_EMAIL_REQUIRED = get_env_variable("ACCOUNT_EMAIL_REQUIRED") == "True"
ACCOUNT_EMAIL_VERIFICATION = get_env_variable("ACCOUNT_EMAIL_VERIFICATION")
EMAIL_CONFIRM_REDIRECT_BASE_URL = get_env_variable("EMAIL_CONFIRM_REDIRECT_BASE_URL")
PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL = get_env_variable("PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL")
AUTH_USER_MODEL = get_env_variable("AUTH_USER_MODEL")





AUTH_USER_MODEL = 'authentication.User'

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'authentication.serializers.CustomRegisterSerializer',
}