#!/usr/bin/env python3
"""Module for client-server application with JSON serialization."""
import socket
import json


def start_server(host='localhost', port=12345):
    """
    Start a server that listens for incoming connections and
    deserializes received JSON data.

    Args:
        host: The hostname to bind to.
        port: The port number to listen on.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, port))
        server_socket.listen(1)

        conn, addr = server_socket.accept()

        try:
            data = b""
            while True:
                chunk = conn.recv(4096)
                if not chunk:
                    break
                data += chunk

            received_dict = json.loads(data.decode("utf-8"))
            print("Received Dictionary from Client:")
            print(received_dict)
        finally:
            conn.close()
    finally:
        server_socket.close()


def send_data(data, host='localhost', port=12345):
    """
    Send a serialized Python dictionary to the server.

    Args:
        data: A Python dictionary to send.
        host: The server hostname.
        port: The server port number.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        serialized = json.dumps(data).encode("utf-8")
        client_socket.sendall(serialized)
    finally:
        client_socket.close()
