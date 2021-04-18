import socket
from contextlib import contextmanager

HOST = "127.0.0.1"  # localhost
PORT = 9999

ADDR_FAM = socket.AF_INET  # IPv4
SOCK_TYPE = socket.SOCK_STREAM  # TCP


@contextmanager
def connected_server() -> (socket.SocketType, tuple):
    try:
        with socket.socket(ADDR_FAM, SOCK_TYPE) as s:
            s.bind((HOST, PORT))
            s.listen()

            yield s.accept()  # client_sock, client_addr
    finally:
        print("Server: Client disconnected")


@contextmanager
def connected_client() -> socket.SocketType:
    try:
        with socket.socket(ADDR_FAM, SOCK_TYPE) as s:
            s.connect((HOST, PORT))

            yield s
    finally:
        print("Client: Disconnected")


def numbers():
    return list(range(10))
