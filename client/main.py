import socket
from network.handle_msg import MessageHandler
import json
import gui
from PyQt6.QtWidgets import (QApplication)
import sys
import threading


class Client:
    HOST = 'localhost'
    PORT = 12345
    def __init__(self,gui):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.HOST, self.PORT))
        self.file = self.socket.makefile("r")
        self.msg_handler = MessageHandler(gui)
        thread = threading.Thread(target=self.start_gui, args=(self,))
        thread.start()
        self.server()
        

    def server(self):
        connected = True
        
        while connected:
            message = self.file.readline().strip()
            message = json.loads(message)
            print("message: ")

            if not message:
                print("Connection closed")
                connected = False
            self.msg_handler.handle_msg(message)

    def start_gui(self):
        app = QApplication(sys.argv)
        window = gui.MainWindow(self)
        window.show()
        app.exec()
    


    def send_server(self,message):
        json_message = json.dumps(message)
        self.socket.send(str(json_message).encode("utf-8"))
        


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
            "msg":"game_cancel",
            "ships": ships
        }
        self.send_server(dic)

    def game_hit(self,x,y):
        dic = {
            "msg":"game_hit",
            "x": x,
            "y": y}
        self.send_server(dic)
            