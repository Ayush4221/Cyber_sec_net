import socket 

host = 'localhost'
port = 12345 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host,port))

data = input("Enter two numbers separated by a comma(EX: '4,2'): ")
client_socket.send(data.encode('utf-8'))
response = client_socket.recv(1024).decode('utf-8')

print("Received from server:", response)

client_socket.close()