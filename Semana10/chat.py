import socket
import threading
import sys

# Server code
def start_server(host='127.0.0.1', port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Server listening on {host}:{port}")

    clients = []
    names = {}

    def broadcast(message, sender):
        for client in clients:
            if client != sender:
                client.send(message)

    def handle_client(client):
        try:
            name = client.recv(1024).decode()  # Receive name first
            names[client] = name
            welcome = f"{name} has joined the chat!"
            broadcast(welcome.encode(), client)
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                full_msg = f"{name}: {msg.decode()}"
                broadcast(full_msg.encode(), client)
        except:
            pass
        finally:
            clients.remove(client)
            left_msg = f"{names.get(client, 'Someone')} has left the chat."
            broadcast(left_msg.encode(), client)
            client.close()
            names.pop(client, None)

    while True:
        client, addr = server.accept()
        print(f"Connected by {addr}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()

start_server()