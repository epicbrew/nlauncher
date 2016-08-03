import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, server_root):
        self.server_root = server_root

    def get(self):
        with open(os.path.join(server_root, 'index.html')) as f:
            self.write(f.read())

