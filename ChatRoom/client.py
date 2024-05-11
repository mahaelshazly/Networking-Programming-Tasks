import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7000))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                # If 'NICK', Send Nickname
                client.send(nickname.encode('ascii'))
            else:
                # Print Other Messages
                print(message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break
        
# Sending Messages To Server
def write():
    while True:
        # Construct Message with Nickname
        message = '{}: {}'.format(nickname, input(''))
        # Send Message to Server
        client.send(message.encode('ascii'))
        
# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
