import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 12345       # The port used by the server

# TODO  Create a server and client, which will use user datagram protocol (UDP) for communication.
# TODO Extend the echo server, which returns to client the data,
#  encrypted using the Caesar cipher algorithm by a specific key obtained from the client.


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'PING')
    data = s.recv(1024)

print('Received', data.decode("utf-8"))
