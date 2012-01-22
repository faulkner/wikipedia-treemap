"""
I was told not to include the source logs.  This script will generate similar fake data to play with.
"""
import json, random

def generate(date):
    # NOTE: these lists are incomplete
    agents = [('Pantech', 'P7000'), ('Samsung', 'SGH-F490'), ('LG', 'KS360'), ('LG', 'GD330'), ('LG', 'LG-P525'), ('SonyEricsson', 'F305'), ('Softbank', 'DM002SH'), ('Alcatel', 'OT-880A'), ('SonyEricsson', 'C510'), ('Samsung', 'SGH-F250L'), ('Cricket', 'A210'), ('LG', 'GR500'), ('Motorola', 'W7'), ('SonyEricsson', 'K790a'), ('Motorola', 'W5'), ('Samsung', 'SGH A167'), ('Motorola', 'V550'), ('LG', 'LG-GT350'), ('Nokia', 'N97i'), ('SonyEricsson', 'W395'), ('Samsung', 'GT B5310'), ('LG', 'GS390'), ('Samsung', 'SGH i900v')]
    countries = ['BD', 'BE', 'BF', 'BG', 'BA', 'BB', 'BM', 'BN', 'BO', 'JP', 'BT', 'JM', 'JO', 'BR', 'BS', 'JE', 'BY', 'BZ', 'RU', 'RW', 'RS', 'TL', 'RE', 'A2', 'RO', 'PG', 'GU', 'GT', 'GR', 'GQ', 'GP', 'BH', 'GY', 'GG', 'GE', 'GD', 'GB', 'GA', 'GM', 'GL', 'GI']
    languages = ['sco', 'scn', 'wuu', 'pnb', 'gu', 'gd', 'ga', 'gn', 'gl', 'als', 'lg', 'hak', 'lb', 'la', 'tt', 'tr', 'cbk-zam', 'li', 'lv', 'lt', 'vec', 'th', 'tg', 'he', 'ksh', 'ta', 'yi', 'de', 'da', 'hif', 'dv', 'qu', 'vls', 'bar', 'eml', 'bpy', 'mhr', 'diq', 'el', 'eo', 'en']

    js = []
    for country in countries:
        for language in languages:
            for (major, minor) in agents:
                js.append({'size': random.randint(1, 1000),
                           'major': major,
                           'minor': minor,
                           'country': country,
                           'lang': language,
                           'site': 'wikipedia',
                           'date': date})

    return json.dumps(js, indent=2)

if __name__ == "__main__":
    for date in ['2000-01-01', '2000-01-02', '2000-01-03']:
        js = generate(date)
        open('../data/%s.json' % date, 'w+').write(js)