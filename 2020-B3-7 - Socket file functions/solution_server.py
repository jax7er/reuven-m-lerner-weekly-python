import socket_util
import pickle
from pathlib import Path
import importlib
from inspect import getmembers, isfunction

modules = [
    importlib.import_module(module_path.name[:-3])
    for module_path in Path().glob("server_func_*.py")
]

actions = {
    name: func 
    for module in modules
    for name, func in getmembers(module) 
    if isfunction(func)
}


with socket_util.connected_server() as (client_sock, client_addr):
    print(client_addr, "connected")
    
    while True:
        if (rx := client_sock.recv(1024)):
            cmd, args = pickle.loads(rx)

            if cmd == "bye":
                break
            elif cmd not in actions:
                tx = pickle.dumps(f"Command {cmd} not found")
            else:
                tx = pickle.dumps(actions[cmd](*args))

            client_sock.send(tx)
