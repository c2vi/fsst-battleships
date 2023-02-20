import socket
import threading
import json
from handle_msg import handle_msg
import toml

class Server():
    def __init__(self):
        super().__init__()
        self.server = None
        self.conn = None
        self.addr = None
        self.Port = 50000
        self.IP = socket.gethostname()
        self.ADDR = (self.IP,self.Port)
        
        # load config from config.toml
        with open ('config.toml', 'r') as f:
          toml_string = f.read()
          parsed_toml= toml.loads(toml_string)
          self.config = parsed_toml

    def handle_socket(self):

        sock_file = self.server.makefile()
        msg = (json.dumps({"msg": "player-list", "players": self.Dict}) + "\n")
        sock_file.write(msg)
        for line in sock_file:
            handle_msg(json.loads(line))








    def start_server(self):
        self.Playerlist=[]
        self.Dict = {}
        self.counter = 0
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen(10)
        while True:
            self.conn, self.addr = self.server.accept()
            thread = threading.Thread(target=self.handle_socket)
            thread.start()
            self.Playerlist.append(self.addr)
            self.Dict[self.counter] = self.counter
            self.counter = self.counter + 1






if __name__ == '__main__':

    server = Server()
    server.start_server()
