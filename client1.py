import socket
import sys

def main():
    host = '127.0.0.1'
    port = 12345        # Server Port

    try:
        # Create socket and connect to server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        message = str(input("Enter a string:"))
        client_socket.sendall(message.encode())  

        response = client_socket.recv(1024).decode()  
        print(f"Server Response: {response}")

        client_socket.close() 
    except Exception as e:
        print(f"Connection error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
