import socket

def main():
    host = '127.0.0.1'  # Server IP
    port = 12345        # Port to connect

    while True:
        print("\nMenu:")
        print("1. Change case of a string")
        print("2. Evaluate a mathematical expression")
        print("3. Find the reverse of a string")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '4':
            print("Exiting...")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice, try again.")
            continue

        data = input("Enter input data: ")
        message = f"{choice}|{data}"  # Format message as "choice|data"

        try:
            # Create socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))  # Connect to server

            client_socket.sendall(message.encode())  # Send message
            response = client_socket.recv(1024).decode()  # Receive response
            print("Server Response:", response)

            client_socket.close()  # Close connection
        except Exception as e:
            print(f"Connection error: {e}")

if __name__ == "__main__":
    main()
