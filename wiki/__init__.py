import os
import tornado.autoreload
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import options
import tornado.web

from wiki.configs import options_setup
import wiki.handlers as h

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", h.HomeHandler),
            (r"/data/([^/]+)?", h.data.DataHandler),
            (r"/(.*)", tornado.web.StaticFileHandler, {'path': os.path.dirname(os.path.dirname(__file__))+'/public'}),
        ]

        settings = dict(
            cookie_secret=options.cookie_secret,
            debug=options.debug,
            static_path=options.static_path,
            template_path=options.template_path,
        )

        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_config_file(os.path.join(os.path.dirname(__file__), "configs/settings.py"))
    tornado.options.parse_command_line()
    tornado.httpserver.HTTPServer(Application()).listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
