import socket
import threading
import json
import handle_msg
import toml
import signal



def check_client_data(player, msg, server):
    handlers = {

        "player_list": handle_msg.player_list,
        "set_name": handle_msg.set_name,
        "match_req": handle_msg.match_req,
        "match_req_cancel": handle_msg.match_req_cancel,
        "match_ack": handle_msg.match_ack,
        "match_deny": handle_msg.match_deny,
        "game_start": handle_msg.game_start,
        "game_cancel": handle_msg.game_cancel,
        "game_place": handle_msg.game_place,
        "game_place_invalid": handle_msg.game_place_invalid,
        "game_do_hit": handle_msg.game_do_hit,
        "game_hit": handle_msg.game_hit,
        "game_hit_success": handle_msg.game_hit_success,
        "set_score": handle_msg.set_score,
        "error": handle_msg.error

    }

    def message_not_found(player, msg, server):
        print("JSON Message is not aviable in the dictonary")

    handler = handlers.get(msg["msg"], message_not_found)
    handler(player, msg, server)


def handle_socket(data, player):
    print("New Player connected")
    sock_file = player.conn.makefile("r")
    msg = json.dumps({"msg": "player_list", "players": data.get_players()}) + "\n"

    for player in server.players.values():
        player.conn.send((msg + "").encode("utf-8"))

    for line in sock_file:
        print("GOT: ", line)
        try:
            msg = json.loads(line)
        except:
            msg = "what you sent was not valid JSON"
            player.conn.send(msg.encode("utf-8"))

        check_client_data(player, msg, data)


class Server():
    def __init__(self):
        super().__init__()
        self.server = None
        self.conn = None
        self.addr = None
        self.Port = 3005
        self.IP = "0.0.0.0"
        self.ADDR = (self.IP, self.Port)

    def start_server(self):
        self.Id = 0
        self.players = {}
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.ADDR)
        self.server.listen(10)
        while True:
            conn, self.addr = self.server.accept()
            player = Player(self.Id, conn)
            self.players[self.Id] = player
            thread = threading.Thread(target=handle_socket, args=(self, player))
            thread.start()
            self.Id = self.Id + 1

    def get_players(self):
        players = []
        for player in self.players.values():
            players.append({
                "name": player.player_name,
                "id": player.Id
                })

        return players


class Player():

    def set_name(self, name):
        self.player_name = name
        return self.player_name

    def __init__(self, Id, conn):
        super().__init__()
        self.Id = Id
        self.conn = conn
        self.player_name = "No Name Yet"


class game():
    def ad(self):
        self.pl = 0

def signal_handler(sig, frame):
    print("recieved SIGINT")
    server.server.close()

if __name__ == '__main__':
    server = Server()
    #signal.signal(signal.SIGINT, signal_handler)
    server.start_server()
