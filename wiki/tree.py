"""
A pile of hacky code to convert flat JSON into the nested structure d3's treemap layout expects.

TODO:
- arbitrary nesting support
- refactor (lots of redundant one-off methods)
"""
from collections import defaultdict

class hash(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

def node(name, children):
    return {'name': name, 'children': children}

def leaf(d):
    return {'name': d['name'], 'size': d['size']}

def group_by(data, field):
    grouped = defaultdict(list)
    for d in data:
        key = d[field]
        grouped[key].append(d)

    return grouped

def sum_group(data, field):
    for k, v in group_by(data, field).items():
        entry = v[0]
        entry['size'] = sum([k['size'] for k in v])
        yield entry

def is_mobile(agent):
    # TODO: this list is incomplete
    agents = ['Android', 'Apple', 'BlackBerry', 'RIM', 'Windows CE', 'DoCoMo', 'Apple iPad', 'Apple iPod', 'Tablet on Android', 'Apple iPhone', 'HipTop', 'Kindle', 'LGE', 'Linux arm',
              'Mobile', 'MIDP', 'NetFront', 'Nintendo', 'Nokia', 'Obigo', 'Opera Mini', 'Opera Mobi', 'Palm Pre', 'Opera Tablet on Android', 'HTC', 'Alcatel', 'LG', 'Motorola',
              'Playstation', 'Samsung', 'SoftBank', 'SonyEricsson', 'SymbianOS', 'UP.Browser', 'Vodafone', 'WAP', 'webOS', 'Wikiamo', 'Wikipanion', 'MyPhone', 'VODAFONE', 'Palm']

    if agent.strip() and any(filter(lambda k: agent.startswith(k), agents)):
        return True

    return False

class Tree(object):
    def __init__(self, data):
        self.data = data

    def flat(self):
        """no nesting at all - one record per cell"""
        return node('wiki', [leaf(d) for d in self.data])

    def mobile(self):
        """only mobile"""
        grouped = defaultdict(list)

        data = filter(lambda k: is_mobile(k['name']), self.data)

        for d in sum_group(data, 'name'):
            grouped[d['major']].append(leaf(d))

        children = [node(name, data) for name, data in grouped.items()]
        return node('wiki', children)

    def nonmobile(self):
        """only non-mobile"""
        grouped = defaultdict(list)

        data = filter(lambda k: not is_mobile(k['name']), self.data)

        for d in sum_group(data, 'name'):
            grouped[d['major']].append(leaf(d))

        children = [node(name, data) for name, data in grouped.items()]
        return node('wiki', children)

    def country(self):
        """group by country"""
        for d in self.data:
            d['name'] = d['country']

        children = [leaf(d) for d in sum_group(self.data, 'name')]
        return node('wiki', children)

    def country_browser(self):
        """group by country, then by browser"""
        grouped = defaultdict(list)
        for d in sum_group(self.data, 'name'):
            key = '%s %s' % (d['country'], d['name'])
            child = {'name': '%s: %s' % (d['name'], d['country']),
                     'size': d['size']}
            grouped[key].append(child)

        children = [node(name, data) for name, data in grouped.items()]
        return node('wiki', children)

    def browser_country(self):
        """group by browser, then by country"""
        grouped = defaultdict(list)
        for d in sum_group(self.data, 'country'):
            key = '%s %s' % (d['name'], d['country'])
            child = {'name': '%s: %s' % (d['name'], d['country']),
                     'size': d['size']}
            grouped[key].append(child)

        children = [node(name, data) for name, data in grouped.items()]
        return node('wiki', children)

    def browser_language(self):
        """group by browser, then by language (probably not super-interesting)"""
        grouped = defaultdict(list)
        for d in sum_group(self.data, 'lang'):
            key = '%s %s %s' % (d['major'], d['minor'], d['lang'])
            child = {'name': '%s: %s' % (d['name'], d['lang']),
                    'size': d['size']}
            grouped[key].append(child)

        children = [node(name, data) for name, data in grouped.items()]
        return node('wiki', children)

    def group_by_mobile(self):
        """group by type of browser (mobile vs non-mobile)"""
        return node('wiki', [
            node('mobile', self.mobile()['children']),
            node('non-mobile', self.nonmobile()['children'])])

    def fake(self):
        """sometimes you just need some fixture data"""
        mobile = [{'name': 'Apple iPhone', 'size': 3938},
                  {'name': 'Nokia', 'size': 3812},
                  {'name': 'Samsung', 'size': 6714},]

        nonmobile = [{'name': 'Chrome', 'size': 3534},
                     {'name': 'Safari', 'size': 5731},
                     {'name': 'Firefox', 'size': 7840},
                     node('IE', [{'name': 'IE 6', 'size': 354},
                                 {'name': 'IE 7', 'size': 571},
                                 {'name': 'IE 8', 'size': 780},]),]

        return node('wiki', [
            node('mobile', mobile),
            node('non-mobile', nonmobile)])
