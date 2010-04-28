'''
Created on Apr 27, 2010
'''

import config
import os

import logging
import wsgiref.handlers
from google.appengine.ext import webapp
from controllers import http, error

# Log a message each time this module get loaded.
logging.info('Loading %s, app version = %s',
             __name__, os.getenv('CURRENT_VERSION_ID'))

ROUTES = [
    ('/*$', http.RootHandler),
    ('/403.html', error.UnauthorizedHandler),
    ('/404.html', error.NotFoundHandler)]

def main():
    application = webapp.WSGIApplication(ROUTES, debug=config.DEBUG)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()