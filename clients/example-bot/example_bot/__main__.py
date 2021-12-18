import socketserver
from .submission_reader import SubmissionReader

socketserver.TCPServer.allow_reuse_address = True
server = socketserver.TCPServer(("localhost", 9999), SubmissionReader)
server.serve_forever()
