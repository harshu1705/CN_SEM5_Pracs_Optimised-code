import socket

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('127.0.0.1', 50003))
        print("Connected to server")
        while (data := input("Enter data (or 'exit' to quit): ")) != 'exit':
            client_socket.send(data.encode())

start_client()

