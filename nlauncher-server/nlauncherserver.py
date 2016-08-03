import sys
import os
import tornado.ioloop
import tornado.web

root = os.path.dirname(__file__)
sys.path.append(root)

from handlers.data import AppDataHandler


def make_app():
    static_path = os.path.join(root, "public")

    settings = {
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        "login_url": "/login",
        "xsrf_cookies": True,
    }

    application = tornado.web.Application([
        (r"/applications", AppDataHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": static_path, "default_filename": "index.html"}),
    ], **settings)

    return application

def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
