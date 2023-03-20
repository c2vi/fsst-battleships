import socket
from network.handle_msg import MessageHandler
import json
from gui.main import MainWindow
from PyQt6.QtWidgets import (QApplication, QWidget)
from PyQt6 import QtCore
import sys
import threading
import select


class Client(QWidget):
    HOST = 'localhost'
    PORT = 3005
    signal = QtCore.pyqtSignal(object)

    def __init__(self, app):
        super().__init__()
        
        self.app = app
        window = MainWindow(self)
        window.show()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.HOST, self.PORT))

        self.file = self.socket.makefile("r")

        self.msg_handler = MessageHandler(window, self)

        self.thread = threading.Thread(target=self.server)
        self.thread.start()

        self.start_gui()


    def server(self):
        connected = True
        
        while connected:
            message = self.file.readline().strip()
            print("GOT: ", message)
            message = json.loads(message)

            if not message:
                print("Connection closed")
                connected = False
            self.msg_handler.handle_msg(message)

    def start_gui(self):
        self.app.exec()
    


    def send_server(self,message):
        json_message = json.dumps(message)
        self.socket.send((json_message + "\n").encode("utf-8"))

        #thread = threading.Thread(target = self.socket.send, args=[json_message.encode("utf-8")])
        #thread.start()
        


    def set_name(self,name):
        dic = {
            "msg":"set_name",
            "name": name
        }
        self.send_server(dic)

    def match_req(self,player_id):
        dic = {
            "msg":"match_req",
            "player_id": player_id
        }
        self.send_server(dic)

    def match_ack(self,player_id):
        dic = {
            "msg":"match_ack",
            "player_id" : player_id
        }
        self.send_server(dic)

    def match_deny(self,player_id):
        dic = {
            "msg":"match_deny",
            "player_id" : player_id
        }
        self.send_server(dic)

    def game_cancel(self):
        dic = {
            "msg":"game_cancel"
        }
        self.send_server(dic)

    def game_place(self,ships):
        dic = {
            "msg":"game_place",
            "ships": ships
        }
        self.send_server(dic)

    def game_hit(self,x,y):
        dic = {
            "msg":"game_hit",
            "x": x,
            "y": y}
        self.send_server(dic)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Client(app)
