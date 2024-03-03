from client import handle_client
import socket
import multiprocessing


def main():
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
            print(f"Accepted connection from {client_address}")
            # Start a new process to handle the client
            process = multiprocessing.Process(target=handle_client, args=(client_socket, client_address))
            process.start()

            # Close the client socket in the parent process
            client_socket.close()

    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        # Close the server socket
        server_socket.close()


if __name__ == "__main__":
    main()
