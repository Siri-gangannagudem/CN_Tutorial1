import socket
import time

def reverse_string(s):
    return s[::-1]

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Only 1 client at a time
    print(f"Single-Process Server running on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()  # Accept client
        print(f"Connected by {addr}")

        data = conn.recv(1024).decode()
        if not data:
            conn.close()
            continue

        time.sleep(3)  # Simulated delay

        response = reverse_string(data)
        conn.sendall(response.encode())

        conn.close()  # Close connection

if __name__ == "__main__":
    main()
