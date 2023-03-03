import socket
import network.handle_msg as handle_msg 
import gui.main 
from gui.main import MainWindow
import threading


class  Client:
    def __init__(self):
        threading.Thread = 
        #TODO: Run connect_server in a other thread
        gui = MainWindow
        #
    def connect_server():
        HOST = 'localhost'
        PORT = 12345
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        file = sock.makefile("r")


        while True:
            message = file.readline().strip()
            
            if not message:
                print("Connection closed")
                break
            handle_msg.handle_msg(message)
            


        