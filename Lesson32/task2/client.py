import socket
import time

HOST, PORT = "localhost", 8080
data = "Hello World!"


def client(host: str, port: int, message: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(message + "\n", "utf-8"))
        response = str(sock.recv(1024), "utf-8")
        print(f"Received: {response}")


if __name__ == "__main__":
    while True:
        client(HOST, PORT, data)
        time.sleep(2)
