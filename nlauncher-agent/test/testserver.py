import tornado.ioloop
import tornado.web


class AppTestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test_form.html')


def make_app():
    return tornado.web.Application([
        (r"/", AppTestHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8887)
    tornado.ioloop.IOLoop.current().start()
