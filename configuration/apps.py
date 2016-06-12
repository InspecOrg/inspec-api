# -*- coding: utf-8 -*-

# Middleware Classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Default Django apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles')

# Django plugins apps
PLUGINS_APPS = (
    'tastypie',
#    'django_nose',
)

# Busine.me application apps
BUSINEME_APPS = (
    'api',
    'importer',
)

INSTALLED_APPS = DJANGO_APPS + PLUGINS_APPS + BUSINEME_APPS
