'''
Created on Apr 27, 2010
'''

import logging
import view

from google.appengine.ext import webapp

class RootHandler(webapp.RequestHandler):
    def get(self):
        logging.debug("RootHandler#get")
        view.Page().render_query(self, '', '', '')

    def post(self):
        logging.debug("RootHandler#post")
