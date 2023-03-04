import socket
import matchmaking
import json

#sends and recieves messages

def network():

    HOST = 'localhost'
    PORT = 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    file = sock.makefile("")

    def set_name():

        msg= json.dumps({"msg":"set-name"})

    while True:
        message = file.readline().strip()

        if not message:
            print("Connection closed")
            break
        print(message)