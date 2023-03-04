import socket
import handle_msg
import json


class Network:
    HOST = 'localhost'
    PORT = 12345
    def __init__(self,gui):
        Network.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Network.socket.connect((self.HOST, self.PORT))
        self.file = Network.socket.makefile("r")
        self.msg_handler = handle_msg.MessageHandler(gui)

    def server(self):
        connected = True
        
        while connected:
            message = self.file.readline().strip()
            message = json.loads(message)

            if not message:
                print("Connection closed")
                connected = False
            self.msg_handler.handle_msg(message)
