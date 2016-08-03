import tornado.ioloop
import tornado.web
from Application import Application


class AppStartHandler(tornado.web.RequestHandler):
    def initialize(self, agent):
        self.agent = agent

    # def get(self):
    #     self.write("Hello, world")

    def post(self):
        try:
            app_id, command = self.validate_arguments()
        except tornado.web.MissingArgumentError:
            return

        app = Application(app_id, command, self.agent)
        app.start()

        agent.add_running_application(app_id, app)

        self.write(dict(
            app_id=app_id,
            command=command,
            result="started"
        ))

    def validate_arguments(self):
        try:
            app_id = self.get_body_argument('app_id')
        except tornado.web.MissingArgumentError:
            self.write(dict(
                result="BadArgumentsError",
                reason="Missing app_id"
            ))
            raise

        try:
            command = self.get_body_argument('command')
        except tornado.web.MissingArgumentError:
            self.write(dict(
                result="BadArgumentsError",
                reason="Missing 'command'"
            ))
            raise

        return app_id, command


class AppStopHandler(tornado.web.RequestHandler):
    def initialize(self, agent):
        self.agent = agent

    def get(self):
        self.write("Hello, world")

    def post(self):
        try:
            app_id = self.get_body_argument('app_id')
        except tornado.web.MissingArgumentError:
            self.write(dict(
                result="BadArgumentsError",
                reason="Missing 'app_id'"
            ))
            return

        if app_id not in self.agent.applications:
            self.write(dict(
                result="NoSuchApplicationError",
                reason="%s is not running" % app_id
            ))
        else:
            app = self.agent.applications[app_id]
            app.stop()
            self.write(dict(
                app_id=app_id,
                result="stopping"
            ))


class NlauncherAgent(object):
    """Main nLauncher agent class."""

    def __init__(self):
        self.applications = {}

    def make_server(self):
        return tornado.web.Application([
            (r"/start", AppStartHandler, dict(agent=self)),
            (r"/stop", AppStopHandler, dict(agent=self)),
        ])

    def add_running_application(self, app_id, app_obj):
        self.applications[app_id] = app_obj

    def app_started(self, app_id):
        print 'agent: %s started' % app_id

    def app_stopped(self, app_id):
        print 'agent: %s stopped' % app_id
        if app_id in self.applications:
            del self.applications[app_id]
        else:
            print 'agent: error: %s stopped but is unknown' % app_id

if __name__ == "__main__":
    agent = NlauncherAgent()
    server = agent.make_server()
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
