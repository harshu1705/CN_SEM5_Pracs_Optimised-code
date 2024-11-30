import socket, threading, time

bucket_token_list, MAX_BUCKET_SIZE, TIME_LAPSE = [], 10, 3
lock = threading.Lock()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('127.0.0.1', 50003))
        server_socket.listen(5)
        print("Server started on 127.0.0.1:50003")
        threading.Thread(target=add_token_to_bucket, daemon=True).start()
        
        while True:
            client_socket, _ = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

def add_token_to_bucket():
    while True:
        with lock:
            if len(bucket_token_list) < MAX_BUCKET_SIZE:
                bucket_token_list.append(1)
        time.sleep(TIME_LAPSE)

def handle_client(client_socket):
    with client_socket:
        while True:
            data = client_socket.recv(1024).decode()
            if data:
                print(f"Received: {data}")
                with lock:
                    if bucket_token_list:
                        bucket_token_list.pop(0)
                        print(f"Token used, bucket: {bucket_token_list}")
                    else:
                        client_socket.send("Token not available, wait.".encode())
                        print("No token available")

start_server()
