def send_server(message):
    pass



def set_name(name):
    dic = {"name": name}
    send_server(dic)

def match_req(player_id):
    dic = {"player_id": player_id}
    send_server(dic)

def match_ack(player_id):
    dic = {"player_id": player_id}
    send_server(dic)

def match_deny(player_id):
    dic = {"player_id": player_id}
    send_server(dic)

def game_cancel():
    dic = {"game_cancel":""}
    send_server(dic)

def game_place(ships):
    dic = {"game_place": ships}
    send_server(dic)

def game_hit(x,y):
    dic = {"game_hit": {"x": x, "y": y}}
    send_server(dic)















    