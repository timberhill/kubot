import socketserver
import json

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        data = self.data.decode('utf8').replace("'", '"')
        print(json.loads(data))
        # just send back the same data, but upper-cased
        self.request.sendall(json.dumps(dict(status=0), indent=2).encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9997

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()