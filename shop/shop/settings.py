"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(key='SECRET_KEY')

# "PASSWORD": os.getenv("POSTGRES_PASSWORD")
# django-insecure-1-*iyy=rizxbq&*4$4$+sbe+3)8(oi@gu^6c^sqp4)^946=5=y'
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = bool(os.getenv(key="DEBUG"))
# DEBUG = True
ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]'] # Список строк, представляющих имена хоста / домена, которые может обслуживать этот сайт Django
"""
['.localhost', '127.0.0.1', '[::1]']

Одной из основных функций режима отладки является отображение подробных страниц ошибок. 
Если ваше приложение вызывает исключение, когда оно DEBUG есть True, Django отобразит подробную трассировку, 
включая множество метаданных о вашей среде, таких как все текущие настройки Django (из settings.py)
"""

# Application definition

INSTALLED_APPS = [        # Список строк, обозначающих все приложения, включенные в этой установке Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [        # Словарь, определяющий пакет, в котором модули миграции могут быть найдены для каждого приложения.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

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

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
   "default": {
       "ENGINE": "django.db.backends.postgresql",
       "NAME": "django",
       "USER": "django",
       "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
       "HOST": "localhost",
       "PORT": 5432,
   }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# https://docs.djangoproject.com/en/4.0/topics/logging/#examples
LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'handlers': {
       'console': {
           'class': 'logging.StreamHandler',
           'formatter': 'simple',
       },
   },
   'formatters': {
       'simple': {'format': '%(levelname)s %(asctime)s %(message)s'},
   },
   'loggers': {
       '': {
           'handlers': ['console'],
           'level': 'INFO',
       },
       'django.db.backends': {
           'handlers': ['console'],
           'level': 'ERROR',
       }
   }
}


MY_CUSTOM_VARIABLE = os.getenv("MY_CUSTOM_VARIABLE", None)




