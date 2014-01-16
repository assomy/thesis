# Django settings for ecomstore project.
#import logging
#from sentry.client.handlers import SentryHandler
DEBUG = True
TEMPLATE_DEBUG = DEBUG
import os
CURRENT_PATH = os.path.abspath( os.path.dirname( __file__ ).decode( 'utf-8' ) ).replace( '\\', '/' )
ADMINS = ( 
     ( 'assomy', 'assomy@gmail.com' ),
 )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'thesis.example.db', 
           
               }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join( CURRENT_PATH, 'static' )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!j$2vhi*4^#%*zib9dp3@khtx!az#3_(p^hog4*dds4(eqzb5&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ( 
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
 )

AUTHENTICATION_BACKENDS = ( 
 )

TEMPLATE_CONTEXT_PROCESSORS = ( 
      
    "allauth.context_processors.allauth",
    "allauth.account.context_processors.account"
 )
AUTHENTICATION_BACKENDS = ( 
    "allauth.account.auth_backends.AuthenticationBackend",
 )    
MIDDLEWARE_CLASSES = ( 
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
 )
ROOT_URLCONF = 'thesis.urls'
TEMPLATE_DIRS = ( 
    os.path.join( CURRENT_PATH, 'templates' ),

 )
INTERNAL_IPS = ( '127.0.0.1', )
TEMPLATE_DEBUG = DEBUG
INSTALLED_APPS = ( 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'pdfviewer',
    'django.contrib.admin',
    'bookmarks',   
 )

SITE_NAME = 'Market Place'
META_KEYWORDS = 'buy and sell'
META_DESCRIPTION = 'cars,mobiles,laptop,computer'
TEMPLATE_CONTEXT_PROCESSORS = ( 
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
 #   'ecomstore.utils.context_processors.ecomstore',
 )

