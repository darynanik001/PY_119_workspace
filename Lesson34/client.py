import socket
import asyncio

HOST, PORT, NUMBER_OF_CLIENTS = "localhost", 8080, 10


async def client(host: str, port: str, client_number: int) -> None:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    await asyncio.sleep(2)
    client_socket.connect((host, port))
    client_socket.sendall(f"Hello from client {client_number}".encode())
    response = client_socket.recv(1024)
    print(f"Response from server: {response.decode()}")
    client_socket.close()


async def client_simulation(host: str, port: int, num_clients: int) -> None:
    clients = [client(host, port, i) for i in range(num_clients)]
    await asyncio.gather(*clients)


if __name__ == "__main__":
    # Start client simulation process
    asyncio.run(client_simulation(HOST, PORT, NUMBER_OF_CLIENTS))
