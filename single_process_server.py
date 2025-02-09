import socket

def process_task(data):
    choice, value = data.split('|', 1)
    
    if choice == '1':
        return value.swapcase()  # Swap case
    elif choice == '2':
        try:
            return str(eval(value))  # Evaluate math expression
        except:
            return "Invalid Expression"
    elif choice == '3':
        return value[::-1]  # Reverse string
    else:
        return "Invalid Option"

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Single client at a time
    print(f"Single-Process Server running on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()  # Accept client
        print(f"Connected by {addr}")

        data = conn.recv(1024).decode()
        if not data:
            break

        response = process_task(data)
        conn.sendall(response.encode())

        conn.close()  # Close connection

if __name__ == "__main__":
    main()
