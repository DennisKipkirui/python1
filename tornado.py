import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,Me")

def make_app():
    return tornado.web.Application([(r"/",MainHandler)]),

if__name__== "__main__":
    app = make.app()
    app.listen(8888)
    
    tornado.ioloop.IOLoop.current().start()


