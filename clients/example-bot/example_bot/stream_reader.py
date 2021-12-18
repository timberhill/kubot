import socketserver
import json


class StreamReader(socketserver.BaseRequestHandler):
    """Comment stream reader
    """
    def handle(self):
        """Transform incoming data into json and call process()
        """
        data = self.request.recv(1024**2).strip()
        data = data.decode('utf-8')
        data = json.loads(data)
        self.request.sendall(bytes("0", "utf-8"))

        self.process(data)

    def process(self, data):
        """Process data.
        This function should be overriden.

        Args:
            data (dict): incoming json object
        """
        raise NotImplementedError("Override this function in the child class.")
