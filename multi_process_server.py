import socket
import multiprocessing

def process_task(conn):
    data = conn.recv(1024).decode()
    if not data:
        conn.close()
        return
    
    choice, value = data.split('|', 1)
    if choice == '1':
        response = value.swapcase()  
    elif choice == '2':
        try:
            response = str(eval(value))  
        except:
            response = "Invalid Expression"
    elif choice == '3':
        response = value[::-1]  
    else:
        response = "Invalid Option"
    
    conn.sendall(response.encode())
    conn.close()  

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  
    print(f"Multi-Process Server running on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        
        process = multiprocessing.Process(target=process_task, args=(conn,))
        process.start()

if __name__ == "__main__":
    main()
