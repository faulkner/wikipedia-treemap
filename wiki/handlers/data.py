import json
from tornado.options import options
from wiki.handlers import BaseHandler
from wiki.tree import *

def get_js(filename):
    with open(filename) as f:
        js = json.loads(f.read())
        for j in js:
            j['name'] = '(unknown)' if not j['major'] else '%s %s' % (j['major'], j['minor'])

        return js

class DataHandler(BaseHandler):
    def get(self, name):
        source = self.param('source', 'chunk.json')
        try:
            # TODO: something less ridiculous.  Punching through to Tree after getting tired of writing one-off handlers.
            cache_filename = options.cache_path + '/%s_%s.json' % (source, name)
            try:
                payload = open(cache_filename, 'r').read()
            except IOError, e:
                with open(cache_filename, 'w') as cache:
                    tree = Tree(get_js(options.data_path + '/' + source))
                    payload = json.dumps(getattr(tree, name)())
                    cache.write(payload)
            self.finish(payload)

        except AttributeError, e:
            return self.finish({'error': 'invalid chart type (%s)' % str(e)})
