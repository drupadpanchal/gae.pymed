'''
Created on Apr 27, 2010
'''

import os
import logging

APP_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Debug flag True only on App Engine development environment (dev_appserver.py)
# dev_appserver sets SERVER_SOFTWARE to 'Development/1.0'
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')
logging.info("Starting application in DEBUG mode: %s", DEBUG)

# List of application settings which will be used globally 
APP_SETTINGS = {
    "application_version": "0.0.0",
    "cache_time": 0 if DEBUG else 3600,
    "html_type": "text/html",
    "charset": "utf-8"
}

# List of mime-types this application will use
MIME_TYPE = { 
    "html" : "text/html",
    "gif" : "image/gif",
    "jpg" : "image/jpeg",
    "png" : "image/png",
    "json" : "text/json",
    "css" : "text/css",
    "js" : "text/js" }


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
