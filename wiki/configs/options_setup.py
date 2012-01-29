from tornado.options import define

define("cookie_secret", default="omnomnom", help="cookie secret key")
define("port", default=8888, help="run on the given port", type=int)
define("static_path", type=unicode, default="/static", help="path for the static files")
define("template_path", type=unicode, default="/", help="path for templates")
define("data_path", type=unicode, default="data", help="path for source data")
define("cache_path", type=unicode, default="data/cache", help="path for cached treemaps")
define("debug", default=True, help="enable debug mode?")
