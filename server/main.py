import socket
import threading
import json
import handle_msg


def check_client_data(player, msg, server):
    handlers = {

        "handle_msg": handle_msg.player_list(player, msg, server),
        "handle_msg": handle_msg.set_name(player, msg, server),
        "handle_msg": handle_msg.match_req(player, msg, server),
        "handle_msg": handle_msg.match_req_cancel(player, msg, server),
        "handle_msg": handle_msg.match_ack(player, msg, server),
        "handle_msg": handle_msg.match_deny(player, msg, server),
        "handle_msg": handle_msg.game_start(player, msg, server),
        "handle_msg": handle_msg.game_cancel(player, msg, server),
        "handle_msg": handle_msg.game_place(player, msg, server),
        "handle_msg": handle_msg.game_place_invalid(player, msg, server),
        "handle_msg": handle_msg.game_do_hit(player, msg, server),
        "handle_msg": handle_msg.game_hit(player, msg, server),
        "handle_msg": handle_msg.game_hit_success(player, msg, server),
        "handle_msg": handle_msg.set_score(player, msg, server),
        "handle_msg": handle_msg.error(player, msg, server)

    }

    handlers.get("handle_msg")


def handle_socket(data, player):
    sock_file = data.server.makefile()
    msg = (json.dumps({"msg": "player_list", "Id": data.Id}) + "\n")
    sock_file.send(msg)
    for line in sock_file:
        try:
            msg = json.loads(line)
            check_client_data(player, msg, data)
        except:
            msg = "what you sent was not valid JSON"
            sock_file.send(msg)


class Server():
    def __init__(self):
        super().__init__()
        self.server = None
        self.conn = None
        self.addr = None
        self.Port = 50000
        self.IP = socket.gethostname()
        self.ADDR = (self.IP, self.Port)

    def start_server(self):
        self.Id = 0
        self.players = {}
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen(10)
        while True:
            self.conn, self.addr = self.server.accept()
            player = Player(self.Id, self.conn)
            self.players[self.Id] = player
            thread = threading.Thread(target=handle_socket, args=(self, player))
            thread.start()
            self.Id = self.Id + 1


class Player():

    def set_name(self, name):
        self.player_name = name
        return self.player_name

    def __init__(self, Id, conn):
        super().__init__()
        self.Id = Id
        self.conn = conn
        self.player_name = None


# class game():


if __name__ == '__main__':
    server = Server()
    server.start_server()
