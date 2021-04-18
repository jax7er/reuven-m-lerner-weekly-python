import socket_util
import pickle

with socket_util.connected_client() as sock:
    sock.sendall("numbers".encode())

    rx = pickle.loads(sock.recv(1024))

    print(rx)
    print(type(rx))
