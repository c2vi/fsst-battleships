import json

def player_list(player,msg,server):
    pass

def set_name(player,msg,server):

    player.name = msg["name"]
    msg = (json.dumps({"msg": "player_list", "players": server.get_players()}) + "\n")
    for player in server.players:
        player.conn.send(msg)

def match_req_cancel(player,msg,server):
    player.player_name = msg["name"]

    rec_msg = json.dumps({"msg": "match_req_cancel", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_Id"])
    other_player.sock.send(rec_msg.encode("utf-8"))

def match_ack(player,msg,server):
    other_player = server.players.get(msg["player_Id"])
    rec_msg = json.dumps({"msg": "game_start", "player_id" : player.Id, "player_id" : other_player}) + "\n"

    other_player.sock.send()

def match_deny(player,msg,server):
    rec_msg = json.dumps({"msg": "match_deny", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_Id"])
    other_player.sock.send(rec_msg.encode("utf-8"))



def game_cancel(player,msg,server):
    rec_msg = json.dumps({"msg": "match_deny", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_Id"])
    other_player.sock.send(rec_msg.encode("utf-8"))

def game_place(player,msg,server):
    rec_msg = json.dumps({"msg": "match_req", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_Id"])
    other_player.sock.send(rec_msg.encode("utf-8"))
    player.conn.sock.send(rec_msg.encode("utf-8"))
    player.game(server,rec_msg)


def game_place_invalid(player,msg,server):
    rec_msg = json.dumps({"msg": "game_place_invalid", "player_id": player.Id}) + "\n"
    player.conn.sock.send(rec_msg.encode("utf-8"))

def game_do_hit(player,msg,server):
    pass

def game_hit(player,msg,server):
    pass

def game_hit_success(player,msg,server):
    pass

def set_score(player,msg,server):
    pass

def error(player,msg,server):

    pass