import socket
import asyncio


async def handle_client(client_socket, client_address: str) -> None:
    print(f"Connected to {client_address}")
    while True:
        data = client_socket.recv(1024)
        await asyncio.sleep(0.5)
        if not data:
            break
        client_socket.sendall(data)

    client_socket.close()
    print(f"Connection with {client_address} closed")


async def main() -> None:
    # Server configuration
    host = "localhost"
    port = 8080
    backlog = 5

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(backlog)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print(type(client_socket))
            print(f"Accepted connection from {client_address}")
            # Start a new process to handle the client
            async with asyncio.TaskGroup() as tg:
                task = tg.create_task(handle_client(client_socket, client_address))

            # Close the client socket in the parent process
            client_socket.close()

    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        # Close the server socket
        server_socket.close()


if __name__ == "__main__":
    asyncio.run(main())
