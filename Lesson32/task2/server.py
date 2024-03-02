from concurrent.futures import ThreadPoolExecutor
from socketserver import (
    ThreadingMixIn,
    TCPServer,
    BaseRequestHandler
)
import time
import threading


class ThreadingTCPServer(ThreadingMixIn, TCPServer):
    pass


class MyTCPHandler(BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("Received from {}:".format(self.client_address[0]))
        print(self.data)
        thread = threading.current_thread()
        print(f'Worker thread: name={thread.name}, idnet={threading.get_ident()}, id={threading.get_native_id()}')
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    server = ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    while server:
        ip, port = server.server_address
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
