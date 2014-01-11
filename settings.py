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
    #'django.contrib.sites',
    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'sentry.client.middleware.SentryResponseErrorIdMiddleware',
    #'djangodblog.handlers.DBLogHandler',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
 #   'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
   # 'ecomstore.SSLMiddleware.SSLRedirect',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'tracking.middleware.VisitorTrackingMiddleware',




 )

ROOT_URLCONF = 'thesis.urls'

TEMPLATE_DIRS = ( 
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
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
GOOGLE_CHECKOUT_MERCHANT_KEY = 'VQ3Dxk2W9nofSaxowUL-Dg'
GOOGLE_CHECKOUT_MERCHANT_ID = '754983958834352'
GOOGLE_CHECKOUT_URL = 'https://sandbox.google.com/checkout/api/checkout/v2/merchantCheckout/Merchant/' + GOOGLE_CHECKOUT_MERCHANT_ID
LOGIN_REDIRECT_URL = '/accounts/my_account/'
AUTHNET_POST_URL = 'test.authorize.net'
AUTHNET_POST_PATH = '/gateway/transact.dll'
AUTHNET_LOGIN = '79FANU2eh2nL'
AUTHNET_KEY = '2532gWCb69xrVcw2'
#django profile 
I18N_URLS = False
DEFAULT_AVATAR = os.path.join( MEDIA_ROOT, 'userprofile/generic.jpg' )
AVATAR_WEBSEARCH = True
# 127.0.0.1:8000 Google GOOGLE_MAPS_API_KEY = "ABQIAAAA06IJoYHDPFMx4u3hTtaghxTpH3CbXHjuCVmaTc5MkkU4wO1RRhST5bKY_U7dUG1ZGu1S-n-ukXGNjQ"
GOOGLE_MAPS_KEY="ABQIAAAA4ja5KWtKhHLCwqtAb2UZjBTKeiOerdq57nEFdb-BTrQXdbRqmhS4d36CNCHR_X461MOYDfLAndocLQ"
# Haddock
#GOOGLE_MAPS_API_KEY="ABQIAAAA06IJoYHDPFMx4u3hTtaghxS1mGAeXhF8eEwoOC3WUqD9xSVHbhT_wvgbriWemZzoPwFT5-HqnLJ9-A"
REQUIRE_EMAIL_CONFIRMATION = False
AVATAR_QUOTA = 2
#GEOIP_PATH = "%s/db/" % PROJECT_PATH
TEMPLATE_CONTEXT_PROCESSORS += ( 
        "userprofile.context_processors.css_classes",
 )
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
#AUTH_PROFILE_MODULE = 'demoprofile.profile'
# END of django-profile specific options

