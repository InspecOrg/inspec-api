"""
Django settings for inspecapi project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from configuration import apps, databases, security, statics, tests

# Security configurations
SECRET_KEY = security.SECRET_KEY
DEBUG = security.DEBUG
TEMPLATE_DEBUG = security.TEMPLATE_DEBUG
ALLOWED_HOSTS = security.ALLOWED_HOSTS

# Application definition
INSTALLED_APPS = apps.INSTALLED_APPS
MIDDLEWARE_CLASSES = apps.MIDDLEWARE_CLASSES

# Default URLs
ROOT_URLCONF = 'inspecapi.urls'

# WSGI
WSGI_APPLICATION = 'inspecapi.wsgi.application'

# Database configuration
DATABASES = databases.DATABASES

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = statics.STATIC_URL
STATIC_ROOT = statics.STATIC_ROOT
STATICFILES_DIRS = statics.STATICFILES_DIRS
TEMPLATE_DIRS = statics.TEMPLATE_DIRS

# Tests configuration
TEST_RUNNER = tests.TEST_RUNNER
NOSE_ARGS = tests.NOSE_ARGS

# Tastypie Settings
TASTYPIE_ALLOW_MISSING_SLASH = True
APPEND_SLASH = False
