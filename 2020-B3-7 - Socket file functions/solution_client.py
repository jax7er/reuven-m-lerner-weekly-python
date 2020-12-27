import socket_util
import pickle

do_actions = (
    ("numbers", 5),
    ("reverse_word", "hello"),
    ("unicode_map", "world"),
    ("make_tea", "one sugar"),
    ("bye", None)
)

with socket_util.connected_client() as sock:
    for cmd, *args in do_actions:
        sock.send(pickle.dumps((cmd, args)))
        
        if (rx := sock.recv(1024)):
            data = pickle.loads(rx)

            print(data)
            print(type(data))
