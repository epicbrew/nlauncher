from __future__ import print_function
import sys
import os
import json
import logging
import tornado.ioloop
import tornado.web
from pymongo import MongoClient

root = os.path.dirname(__file__)
sys.path.append(root)

from handlers.data import AppGroupsDataHandler
from nlauncher.state import NlauncherState


def get_database(dbname):
    """Returns a handle to our database."""
    client = MongoClient()
    return client[dbname]


def get_config(config_path):
    print('loading: %s' % config_path)

    with open(config_path, 'r') as f:
        config = json.load(f)

    return config


def init_logging(config):
    numeric_level = getattr(logging, config['log_level'])

    if not isinstance(numeric_level, int):
        logging.critical('Invalid log level: %s' % loglevel)
        sys.exit(1)

    logging.basicConfig(level=numeric_level)


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
    init_logging(config)

    db = get_database(config['database'])
    state = NlauncherState(db)

    state.query_app_state()

    app = make_app(db)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
