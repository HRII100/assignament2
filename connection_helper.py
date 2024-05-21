#!/usr/bin/env python3
# This module defines general functions for establishing an arbitrary TCP connection with a remote host


import socket

def create_connection(url):
    """
    Creates a socket connection to the server.
    Args:
        url (str): The URL to connect to.
    Returns:
        socket: The socket object connected to the server.
    """
    host = url.split('/')[0]
    port = 80
    conn = socket.create_connection((host, port))
    return conn

def send_request(conn, url):
    """
    Sends an HTTP GET request to the server.
    Args:
        conn (socket): The socket object connected to the server.
        url (str): The URL to request.
    """
    host = url.split('/')[0]
    path = '/' + '/'.join(url.split('/')[1:])
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    conn.sendall(request.encode())

def receive_response(conn):
    """
    Receives the HTTP response from the server.
    Args:
        conn (socket): The socket object connected to the server.
    Returns:
        bytes: The raw HTTP response.
    """
    response = bytearray()
    while True:
        chunk = conn.recv(4096)
        if not chunk:
            break
        response.extend(chunk)
    conn.close()
    return response

