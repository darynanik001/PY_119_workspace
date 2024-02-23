from caesar_cipher import caesar_cipher
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ("localhost", 12345)
print("starting up on {} port {}".format(*server_address))
sock.bind(server_address)

while True:
    # Receive message and address from client
    data, client_address = sock.recvfrom(1024)

    # Print the received message and client address
    print(f"Received message from {client_address}: {data.decode()}")

    # Send a response back to the client
    response = "PONG"
    sock.sendto(caesar_cipher(response, "F").encode(), client_address)
