from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/root", perm="elradfmwMT")
authorizer.add_anonymous("/root/Desktop")
handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("192.168.1.154", 21), handler)
server.serve_forever()


