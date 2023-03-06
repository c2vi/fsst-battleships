import socket


HOST = 'localhost'
PORT = 3005
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
file = sock.makefile("r")


while True:
    message = file.readline().strip()
    
    if not message:
        print("Connection closed")
        break
    print(message)
