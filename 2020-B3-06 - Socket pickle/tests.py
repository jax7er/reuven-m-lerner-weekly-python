import pytest
import socket
from threading import Thread

from solution_server import run_server
from solution_client import get_client_socket, send_client_message


@pytest.fixture
def running_server():
    print("Running server")
    t = Thread(target=run_server, daemon=True)
    t.start()
    yield
    print("Tearing down server")


def test_numbers(running_server):
    client_socket = get_client_socket()
    assert send_client_message(client_socket, 'numbers') == list(range(10))


def test_reverse_word(running_server):
    client_socket = get_client_socket()
    assert send_client_message(
        client_socket, 'reverse_word elephant') == 'tnahpele'


def test_unicode_map(running_server):
    client_socket = get_client_socket()
    assert send_client_message(client_socket, 'unicode_map abracadabra') == {
        'a': 97, 'b': 98, 'c': 99, 'd': 100, 'r': 114}