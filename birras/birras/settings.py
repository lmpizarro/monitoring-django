"""
Django settings for birras project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from birras import api_weather_token

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#ghw9(*tnt2d4508x!1su!knm*ud2n7l0-&y&zt)8yj)q4w73a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DOCKER = False

ALLOWED_HOSTS = ['web', 'localhost', '192.168.0.173']


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'app.apps.AppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
    'django_prometheus'
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'birras.urls'

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

WSGI_APPLICATION = 'birras.wsgi.application'

db_name = 'birras'
db_user = 'birras'
db_pass = 'birras'
db_port = '5432'
db_host = 'localhost'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_pass,
        "HOST": db_host,
        'PORT': db_port,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATIC_URL = '/static/'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'
WEATHER_PLACE = 'London,uk' 
WEATHER_APPID = api_weather_token.WEATHER_APPID


redis_host = 'localhost'
if DOCKER:
    redis_host = 'redis'

CELERY_BROKER_URL='redis://{}:6379/0'.format(redis_host)


from celery.schedules import crontab   
CELERY_TIMEZONE = 'UTC'
CELERY_BEAT_SCHEDULE = {
    'update-temperature-every-hour': {
       'task': 'newtemperature',
       'schedule': 10.0,
    },
    #'send-notification-at-midnight': {
    #     'task': 'send_notification',
    #     'schedule': crontab(minute=0, hour=0,),
    #    },
    'send-notification-week-meetup': {
        'task': 'week_meetups',
        'schedule': crontab(minute=0, hour=0, day_of_week='monday'),
    },
}


BOTTLES_MIN = .75
BOX_SIZE = 6
TEMP_MIN = 20
TEMP_MAX = 24

GRAPPELLI_ADMIN_TITLE='Birras'

# Email configuration
EMAIL_HOST='email.com'
EMAIL_HOST=22
EMAIL_FROM='thebirrasmeetup.com'

SERVER_HOST = os.environ.get('SERVERHOST', 'http://localhost:8080/')
