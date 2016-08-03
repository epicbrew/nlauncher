import tornado.web

class AppDataHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(dict(
            groups=[
                { 'name': 'PASFS',
                  'apps': [
                    {'name': 'PASFS CONTROL', 'command': '/sqq89/linux/pasfs/run_pasfs_control'},
                    {'name': 'PASFS 53C', 'command': '/sqq89/linux/pasfs/run_pasfs_53c'},
                  ]
                },
                { 'name': 'BFFS',
                  'apps': [
                    {'name': 'TRB MFTA 1', 'command': '/sqq89/linux/pasfs/run_trbcp1'},
                    {'name': 'HRB 53C 1', 'command': '/sqq89/linux/pasfs/run_hrbcp1'},
                  ]
                },
            ],
        ))

