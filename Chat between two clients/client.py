# client.py

import socket
import threading

def receive_messages(sock):
    """
    Function to continuously receive messages from the server and print them.
    """
    while True:
        try:
            # Receive the size of the incoming message
            size_bytes = sock.recv(8)
            size = int.from_bytes(size_bytes, 'big')
            # Receive the message itself and decode it
            data = sock.recv(size).decode('utf-8')
            print(data)
        except socket.error:
            # Break the loop if there's an error
            break

def send_message(sock):
    """
    Function to send messages to the server.
    """
    while True:
        # Get message and recipient information from user input
        message = input("Enter message: ")
        recipient = input("Enter recipient address (host:port): ")
        # Combine recipient and message into a single string
        data = f"{recipient}:{message}"
        # Send the length of the data as 8-byte big-endian bytes
        sock.send(len(data).to_bytes(8, 'big'))
        # Send the data itself encoded in utf-8
        sock.send(data.encode('utf-8'))

def start_chat():
    """
    Function to start the client chat.
    """
    host = 'localhost'
    port = 8000

    # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # Start thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()

    # Start thread to send messages
    send_thread = threading.Thread(target=send_message, args=(sock,))
    send_thread.start()

if __name__ == '__main__':
    start_chat()
