import socket
import multiprocessing

HOST, PORT, NUMBER_OF_CLIENTS = "localhost", 8080, 3


def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)

    client_socket.close()
    print(f"Connection with {client_address} closed")


def client_simulation(host, port, num_clients):
    for i in range(num_clients):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(f"Hello from client {i}".encode())
        response = client_socket.recv(1024)
        print(f"Response from server: {response.decode()}")
        client_socket.close()


if __name__ == "__main__":
    # Start client simulation process
    client_process = multiprocessing.Process(target=client_simulation, args=(HOST, PORT, NUMBER_OF_CLIENTS))
    client_process.start()