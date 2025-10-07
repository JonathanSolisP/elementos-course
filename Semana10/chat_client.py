import socket
import threading
import sys

# Client code
def start_client(host='127.0.0.1', port=5000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    name = input("Enter your name: ")
    client.send(name.encode())  # Send name to server

    def receive():
        while True:
            try:
                msg = client.recv(1024)
                if not msg:
                    break
                print("\n", msg.decode(), "\nYou: ", end='', flush=True)
            except:
                break

    threading.Thread(target=receive, daemon=True).start()

    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        client.send(msg.encode())
    client.close()

start_client()