class ServerCommunication:
    def __init__(self):
        pass

    def send_server(self, message):
        pass

    def set_name(self, name):
        dic = {"name": name}
        self.send_server(dic)

    def match_req(self, player_id):
        dic = {"player_id": player_id}
        self.send_server(dic)

    def match_ack(self, player_id):
        dic = {"player_id": player_id}
        self.send_server(dic)

    def match_deny(self, player_id):
        dic = {"player_id": player_id}
        self.send_server(dic)

    def game_cancel(self):
        dic = {"game_cancel":""}
        self.send_server(dic)

    def game_place(self, ships):
        dic = {"game_place": ships}
        self.send_server(dic)

    def game_hit(self, x,y):
        dic = {"game_hit": {"x": x, "y": y}}
        self.send_server(dic)















    