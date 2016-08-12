from __future__ import print_function
import tornado.web


class AppGroupsDataHandler(tornado.web.RequestHandler):
    def initialize(self, database):
        self.database = database

    def get(self):
        groups = self.database.groups
        response = []

        for group in groups.find():
            group['_id'] = str(group['_id'])
            response.append(group)

        self.write(dict(groups=response))
