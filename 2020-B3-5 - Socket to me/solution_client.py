import socket


HOST = "127.0.0.1" # localhost
PORT = 9999

ADDR_FAM = socket.AF_INET # IPv4
SOCK_TYPE = socket.SOCK_STREAM # TCP

messages = (
    "hi",
    "say If I die, it means I have lived",
    "increment 10",
    "Do you wish you could?",
    "bye"
)


with socket.socket(ADDR_FAM, SOCK_TYPE) as s:
    s.connect((HOST, PORT))

    for message in messages:
        s.sendall(message.encode())
        
        print(message, "->", s.recv(1024).decode())
