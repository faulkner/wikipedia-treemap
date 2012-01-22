import tornado.escape
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def finish(self, chunk):
        # encode lists; ignore tornado's ridiculous, outdated rant about security holes in ancient browsers
        if isinstance(chunk, dict):
            chunk = tornado.escape.json_encode(chunk)
            self.set_header("Content-Type", "application/json; charset=UTF-8")

        super(BaseHandler, self).finish(chunk)

    def param(self, field, default=None):
        return self.get_argument(field, default)

# TODO: only here because I couldn't find a good way to alias / to index.html from within the router
class HomeHandler(BaseHandler):
    def get(self):
        self.finish(self.render_string('public/index.html'))

import wiki.handlers.data
