'''
Created on Apr 27, 2010
'''

import logging

class Page(object):
    def render_error(self, handler, error):
        logging.debug("Error - %s" % error)
        handler.error(error)
        handler.response.out.write("<html><title>Error: %s</title><body><h3>Error - Respond to Sproutcore view with error message to display</h3></body></html>" % error)
        
    def render_query(self, handler, model_name, query, params={}):
        logging.debug("Render this query using the main html-template")
        handler.response.out.write("<html><title>Main HTML-Page</title><body><h3>Test Page - Replace with Sproutcore main</h3></body></html>")
