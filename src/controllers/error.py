'''
Created on Apr 27, 2010
'''

import logging
import view

from google.appengine.ext import webapp

class UnauthorizedHandler(webapp.RequestHandler):
    def get(self):
        logging.debug("403 - Unauthorized")
        view.Page().render_error(self, 403)

class NotFoundHandler(webapp.RequestHandler):
    def get(self):
        logging.debug("404 - Not Found")
        view.Page().render_error(self, 404)
        
    def post(self):
        raise NotImplementedError()