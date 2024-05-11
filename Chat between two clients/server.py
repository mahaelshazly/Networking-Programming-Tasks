# server.py

import socket
import threading
import ast

def handle_client(client_session, client_address):
    """
    Function to handle communication with a client.
    """
    while True:
        try:
            # Receive the size of the incoming message
            size_bytes = client_session.recv(8)
            size = int.from_bytes(size_bytes, 'big')
            # Receive the message itself and decode it
            data = client_session.recv(size).decode('utf-8')
            if not data:
                break
            print(f"Received from {client_address}: {data} : with size {size}")

            # Extract the recipient client's address from the message
            recipient_address, message = data.split(':', 1)

            # Find the recipient client's socket
            recipient_socket = None
            for client in clients:
                if client[1] == ast.literal_eval(recipient_address):
                    recipient_socket = client[0]
                    break
            if recipient_socket:
                # Send the size of the message to the recipient client
                recipient_socket.send(size_bytes)
                # Send the message itself to the recipient client
                recipient_socket.send(message.encode('utf-8'))
            else:
                print(f"Recipient not found: {recipient_address}")

        except socket.error:
            break

    print(f"Connection closed with {client_address}")
    # Remove the client from the list of active clients
    clients.remove((client_session, client_address))
    client_session.close()

def start_server():
    """
    Function to start the server.
    """
    host = 'localhost'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        # Accept incoming client connections
        client_session, client_address = server_socket.accept()
        # Add the client to the list of active clients
        clients.append((client_session, client_address))
        print(f"Connected with {client_address}")
        # Start a new thread to handle communication with the client
        threading.Thread(target=handle_client, args=(client_session, client_address)).start()

if __name__ == '__main__':
    # Initialize list of active clients
    clients = []
    start_server()
