"""
The original data I was handed was tab-delimited; convert that to json.
"""
import sys, json

if __name__ == "__main__":
    # ghetto arg handling
    if len(sys.argv) != 3:
        raise Exception('usage: convert.py from to')

    (_, from_file, to_file) = sys.argv

    fields = ['size', 'major', 'minor', 'country', 'lang', 'site', 'date']
    f = open(from_file)
    js = [dict(zip(fields, l.strip().split('\t'))) for l in f.readlines()]
    for j in js:
        j['size'] = int(j['size'])
    open(to_file, 'w+').write(json.dumps(js, indent=2))