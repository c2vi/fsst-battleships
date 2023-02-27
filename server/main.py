import socket
import threading
import json
from handle_msg import handle_msg


def handle_socket(self,Id,player):
    sock_file = self.server.makefile()
    msg = (json.dumps({"msg": player, "Id": Id}) + "\n")
    sock_file.write(msg)
    for line in sock_file:
        handle_msg(json.loads(line))

class Server():
    def __init__(self):
        super().__init__()
        self.server = None
        self.conn = None
        self.addr = None
        self.Port = 50000
        self.IP = socket.gethostname()
        self.ADDR = (self.IP,self.Port)


    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen(10)
        while True:
            self.conn, self.addr = self.server.accept()
            thread = threading.Thread()
            thread.start()




class Player(Server):
    def __init__(self):
        super().__init__()

    def player_name(self):
        self.player_name = "set_name(name)"

    def get_player_conn(self):
        self.Id = {}
        self.player={}
        self.counter = 0
        #player_name()
        #self.player[self.player_name()] = self.player_name()
        self.Id[self.counter] = self.counter
        handle_socket(self.Id,self.player)





if __name__ == '__main__':
    player = Player()
    server = Server()
    server.start_server()
