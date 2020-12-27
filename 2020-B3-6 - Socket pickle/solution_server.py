import socket_util
import pickle


with socket_util.connected_server() as (client_sock, client_addr):
    print(client_addr, "connected")
    
    rx = client_sock.recv(1024).decode()

    if rx == "numbers":
        data = pickle.dumps(socket_util.numbers())

        client_sock.sendall(data)
