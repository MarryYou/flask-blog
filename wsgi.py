from app import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

if __name__ == "__main__":
    server = HTTPServer(WSGIContainer(app))
    server.listen(port=3366, address="0.0.0.0")
    IOLoop.instance().start()
