from __future__ import print_function
import sys
import os
import tornado.ioloop
import tornado.web
import json
from pymongo import MongoClient

root = os.path.dirname(__file__)
sys.path.append(root)

from handlers.data import AppGroupsDataHandler


def get_database(dbname):
    """Returns a handle to our database."""
    client = MongoClient()
    return client[dbname]


def get_config(config_path):
    print('loading: %s' % config_path)

    with open(config_path, 'r') as f:
        config = json.load(f)

    return config


def make_app(database):
    static_path = os.path.join(root, "public")

    settings = {
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        "login_url": "/login",
        "xsrf_cookies": True,
    }

    application = tornado.web.Application([
        (r"/applications", AppGroupsDataHandler, dict(database=database)),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": static_path, "default_filename": "index.html"}),
    ], **settings)

    return application


def main():
    if len(sys.argv) != 2:
        print("usage: %s <configfile>.json" % sys.argv[0])
        sys.exit(1)

    config = get_config(sys.argv[1])

    db = get_database(config['database'])

    app = make_app(db)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
