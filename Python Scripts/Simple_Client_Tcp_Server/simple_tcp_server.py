import socket

def handle_client(data: str) -> str:
    try: 
        num1, num2 = data.split(',')
        return str(int(num1) + int(num2))
    except ValueError as e:
        return f"Invalid input: {e}"


def tcp_server(host: str, port: int):
    try:
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
        server_socket.bind((host,port))
       
        server_socket.listen(1)

        client_socket, client_address = server_socket.accept()
        print(f"Connected by {client_address}") 
        print("Waiting for Client Response...")
        while True:
           
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            print(f"Received: {data}")
            message = handle_client(data)
            client_socket.send(message.encode('utf-8'))
            
        client_socket.close()
    except socket.gaierror as e:
        print(f"Address-related error connecting to server: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except  Exception as e: 
        print(f"An error occurred: {e}")
   
tcp_server('localhost', 12345) 