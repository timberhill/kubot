import socketserver

import threading

from .stream_handler import StreamHandler


class KubotClient:
    """Client class, listening data from the dispatcher
    """
    def __init__(self, submission_handler: StreamHandler,
                 comment_handler: StreamHandler):
        self.submission_handler = submission_handler
        self.comment_handler = comment_handler

    def start(self):
        """Start submission and/or comment servers
        """
        socketserver.TCPServer.allow_reuse_address = True

        submission_server = socketserver.TCPServer(
            ("localhost", self.submission_handler.port),
            self.submission_handler
        )

        comment_server = socketserver.TCPServer(
            ("localhost", self.comment_handler.port),
            self.comment_handler
        )

        submission_thread = \
            threading.Thread(target=submission_server.serve_forever)
        comment_thread = \
            threading.Thread(target=comment_server.serve_forever)

        submission_thread.start()
        comment_thread.start()
