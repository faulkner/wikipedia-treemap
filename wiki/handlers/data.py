import json
from wiki.handlers import BaseHandler
from wiki.tree import *

class DataHandler(BaseHandler):
    def get(self, name):
        self.from_file = 'data/' + self.param('source', 'chunk.json')
        try:
			# TODO: something less ridiculous.  Punching through to Tree after getting tired of writing one-off handlers.
            tree = Tree(self._get_js())
            payload = getattr(tree, name)()
            self.finish(payload)
        except AttributeError, e:
            return self.finish({'error': 'invalid chart type (%s)' % str(e)})

    def _get_js(self):
        f = open(self.from_file)
        js = json.loads(f.read())
        for j in js:
            j['name'] =  '(unknown)' if not j['major'] else '%s %s' % (j['major'], j['minor'])

        # TODO: remove range limit once we're caching the results, as otherwise the page just takes too long to load
        return js[0:500]
