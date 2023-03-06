import json

def player_list(player,msg,server):
    pass

def set_name(player,msg,server):

    player.player_name = msg["name"]

    msg = (json.dumps({"msg": "player_list", "players": server.get_players()}) + "\n")
    for player in server.players.values():
        player.conn.send((msg + "").encode("utf-8"))

def match_req_cancel(player,msg,server):
    pass

def match_ack(player,msg,server):
    pass

def match_req(player,msg,server):
    pass

def match_deny(player,msg,server):
    pass

def game_start(player,msg,server):
    pass

def game_cancel(player,msg,server):
    pass

def game_place(player,msg,server):
    pass

def game_place_invalid(player,msg,server):
    pass

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
