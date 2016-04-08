import tornado.web
import tornado.httpserver
from tornado.options import define, options

import config

define("port", default=config.settings['port'], help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, config.handlers, **config.settings)


if __name__ == '__main__':
    app = Application()
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

