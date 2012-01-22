Wikipedia usage treemap
=========

Given a pile of Wikipedia usage stats, build treemaps.

# WARNING: hackathon code
This was cobbled together in a hurry and has gone through some sloppy rewrites.

# Getting up and running

```
pip install -r requirements.txt
coffee -o public/assets/js -c public/assets/coffee
./app.py
```

# Generating sample data

```
scripts/generate.py
```

# TODO
- gut the rest of backbone-boilerplate (was testing it out, but don't need 90% of it)
- add endpoints to lookup existing data sources & chart types (these are hard-coded in the template right now)
- fix nested grouping issues
- caching of generated treemap JSON
- split out model details for phones that include it (ex: RIM BlackBerry 123)
- make data handler more generic
- port backbone code to coffeescript
