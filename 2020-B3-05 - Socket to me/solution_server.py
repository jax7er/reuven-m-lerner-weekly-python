import socket


HOST = "127.0.0.1" # localhost
PORT = 9999

ADDR_FAM = socket.AF_INET # IPv4
SOCK_TYPE = socket.SOCK_STREAM # TCP


with socket.socket(ADDR_FAM, SOCK_TYPE) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen()

    client_sock, client_addr = server_sock.accept()

    with client_sock:
        data = ""
        
        while not data.startswith("bye"):
            data = client_sock.recv(1024).decode()

            if data.startswith("hi"):
                response = "Hello Laura"
            elif data.startswith("bye"):
                response = "Goodbye Laura"
            elif data.startswith("say "):
                response = data[len("say "):]
            elif data.startswith("increment "):
                response = str(int(data[len("increment "):]) + 1)
            else:
                response = "I'm sorry Laura, I don't understand the question"
            
            client_sock.sendall(response.encode())    
