from tornado.options import define

define("cookie_secret", default="omnomnom", help="cookie secret key")
define("port", default=8888, help="run on the given port", type=int)
define("static_path", type=unicode, default="/static", help="path for the static files")
define("template_path", type=unicode, default="/", help="path for templates")
define("debug", default=True, help="enable debug mode?")
