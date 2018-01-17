"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+d@0xti4#$mm&00yu8=2wx48yu0$e8f^&oxi@%gpg!%qgw5fmr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'web201',
	'comments',
	'users',
	'captcha',
	'oauth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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



AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'users.backends.EmailBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'users.User'

LOGOUT_REDIRECT_URL = '/'

LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'


#Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = False

EMAIL_HOST = 'smtpdm.aliyun.com'

EMAIL_PORT = 25

EMAIL_HOST_USER = 'zjw@mail.zjw666.top'

EMAIL_HOST_PASSWORD = 'zjw063616ZJW'

DEFAULT_FROM_EMAIL = 'Marine Geology Office 201 <zjw@mail.zjw666.top>'

#Captcha

CAPTCHA_IMAGE_SIZE = (100,30)

CAPTCHA_FOREGROUND_COLOR = 'red'

CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s %(image)s %(hidden_field)s'


#Oauth

GITHUB_APP_ID = 'e3ae38784d613837fa93'

GITHUB_KEY = '64a26a79c12534bdbd2e84f2d517dd666c0b2ea8'

GITHUB_CALLBACK_URL = 'http://127.0.0.1:8000/oauth/github_check'

QQ_APP_ID = ''

QQ_KEY = ''

QQ_CALLBACK_URL = 'http://127.0.0.1:8000/oauth/qq_check'

WEIBO_APP_ID = '1295041918'

WEIBO_KEY = '368f7e717f6d4ce8eddd8a59f248f0f9'

WEIBO_CALLBACK_URL = 'http://127.0.0.1:8000/oauth/weibo_check'
