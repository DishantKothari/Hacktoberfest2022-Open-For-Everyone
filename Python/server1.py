import socket


def server_program():
    # get the hostname
    host = socket.gethostbyname(socket.gethostname())
    port = 1024  

    server_socket = socket.socket()  
    
    server_socket.bind((host, port))  

    
    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        s
        data = conn.recv(2048).decode()
        if not data:
            
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  

    conn.close()  


if __name__ == '__main__':
    server_program()
