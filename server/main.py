import socket
import threading


class Server():
    def __init__(self):
        super().__init__()
        self.server = None
        self.conn = None
        self.addr = None
        self.Port = 50000
        self.IP = socket.gethostname()
        self.ADDR = (self.IP,self.Port)

    def handle_socket(self):

        self.conn.send(self.addr)

        self.conn.rec(1024)
        sock.makefile("r")
        while True:
            sock.readline()



    def start_server(self):
        self.Playerlist=[]
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen(10)
        while True:
            self.conn, self.addr = self.server.accept()
            thread = threading.Thread(target=self.handle_socket)
            thread.start()
            self.Playerlist.append(self.addr)




if __name__ == '__main__':

    server = Server()
    server.start_server()
