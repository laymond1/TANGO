"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9mzdp6rd_q2&x^@qph9u$a7x!hqz1ndore@#g8t6kf#8x%-73-'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', '*']

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST =[
#     'http://0.0.0.0:3000',  # project_manager - frontend
#     'http://0.0.0.0:8081',  # bms
#     'http://0.0.0.0:8091',  # viz2Code
#     'http://0.0.0.0:8888',  # code gen
#     'http://0.0.0.0:8087',  # autonn bb
#     'http://0.0.0.0:8089',  # autonn nk
#     'http://0.0.0.0:8088',  # cloud deployS
#     'http://0.0.0.0:8891',  # onDevice deploy
# ]

CORS_ALLOW_METHODS = [
    'GET',
    'POST'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'oauth2_provider',
    'corsheaders',
    'tango',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend', 'build'),
        ],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# ---------------------------------------
# CASE I.
# for testing backend at Docker container
# use PostgreSQL
# ---------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'postgresql',
        'PORT': '5432',
    }
}

# ---------------------------------------
# CASE II.
# for testing backend at local host
# use sqlite3
# ---------------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Tango',
#         'USER': 'postgres',
#         'PASSWORD': 'tesla',
#         'HOST': '106.247.227.244',
#         'PORT': '5432',
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',          # 모든 사용자 권한
        'rest_framework.permissions.IsAuthenticated',   # 인증된 사용자 권한
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
}

OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 604800,
    'REFRESH_TOKEN_EXPIRE_SECONDS': 30
}

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.AllowAny',          # 모든 사용자 권한
#         'rest_framework.permissions.IsAuthenticated',   # 인증된 사용자 권한
#         #'rest_framework.permissions.IsAdminUser',       # 관리자 권한
#     ),
#
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#         # 'rest_framework.authentication.TokenAuthentication',
#         # 'rest_framework.authentication.SessionAuthentication',
#         # 'rest_framework.authentication.BasicAuthentication',
#     ),
# }
#
# JWT_AUTH = {
#     'JWT_SECRET_KEY': SECRET_KEY,
#     'JWT_ALGORITHM': 'HS256',
#     'JWT_ALLOW_REFRESH': True,
#     # 'JWT_AUTH_HEADER_PREFIX': 'Bearer', # 추가
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),             # 토큰 유효 시간
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),
# }


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

###
# 20220113 jpchoi
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
###

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'build', 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
