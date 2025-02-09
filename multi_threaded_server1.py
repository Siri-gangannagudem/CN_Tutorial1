import socket
import time
import threading

def handle_client(conn):
    data = conn.recv(1024).decode()
    if not data:
        conn.close()
        return

    time.sleep(3)  # Simulated delay

    response = data[::-1]  # Reverse string
    conn.sendall(response.encode())

    conn.close()  # Close connection

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(10)  # Allow multiple connections
    print(f"Multi-Threaded Server running on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()

if __name__ == "__main__":
    main()
