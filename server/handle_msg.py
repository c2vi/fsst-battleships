import json
SHIP_COUNT = 10

def player_list(player,msg,server):
    pass

def set_name(player,msg,server):

    player.player_name = msg["name"]

    msg = (json.dumps({"msg": "player_list", "players": server.get_players()}) + "\n")
    for player in server.players.values():
        player.conn.send((msg + "").encode("utf-8"))

def match_req_cancel(player,msg,server):
    player.player_name = msg["name"]

    rec_msg = json.dumps({"msg": "match_req_cancel", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_id"])
    other_player.conn.send(rec_msg.encode("utf-8"))

def match_ack(player,msg,server):
    other_player = server.players.get(msg["player_id"])
    rec_msg = json.dumps({"msg": "game_start", "player_id" : player.Id, "other_player_id" : other_player.Id}) + "\n"

    other_player.conn.send(rec_msg.encode("utf-8"))
    player.conn.send(rec_msg.encode("utf-8"))

def match_req(player,msg,server):
    other_player = server.players[msg["player_id"]]
    msg["player_id"] = player.Id
    print(json.dumps(msg))
    other_player.conn.send(json.dumps(msg).encode("utf-8") + b"\n")

def match_deny(player,msg,server):
    rec_msg = json.dumps({"msg": "match_deny", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_id"])
    other_player.conn.send(rec_msg.encode("utf-8"))



def game_cancel(player,msg,server):
    rec_msg = json.dumps({"msg": "match_deny", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_id"])
    other_player.conn.send(rec_msg.encode("utf-8"))

def game_place(player,msg,server):
    rec_msg = json.dumps({"msg": "match_req", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_id"])
    other_player.conn.send(rec_msg.encode("utf-8"))
    player.conn.conn.send(rec_msg.encode("utf-8"))
    player.game(server,rec_msg)


def game_place_invalid(player,msg,server):
    rec_msg = json.dumps({"msg": "game_place_invalid", "player_id": player.Id}) + "\n"
    player.conn.conn.send(rec_msg.encode("utf-8"))


def game_hit(player,msg,server):
    x = msg["x"]
    y = msg["y"]
    other_player = server.players.get(player.opponent_id)
    cell_value = other_player.board[x][y]
    if cell_value == " ":
        # Missed
        other_player.board[x][y] = "O"
        rec_msg = json.dumps({"msg": "game_hit_miss", "player_id": player.Id, "x": x, "y": y}) + "\n"
    elif cell_value == "S":
        # Hit
        other_player.board[x][y] = "X"
        rec_msg = json.dumps({"msg": "game_hit_success", "player_id": player.Id, "x": x, "y": y}) + "\n"
        player.score += 1
        set_score(player, server, player.score)
        if player.score == SHIP_COUNT:
            # Player wins the game
            rec_msg = json.dumps({"msg": "game_over", "player_id": player.Id, "result": "win"}) + "\n"
            player.conn.send(rec_msg.encode("utf-8"))
            other_player.conn.send(rec_msg.encode("utf-8"))
            return
    else:
        # Already hit this cell
        rec_msg = json.dumps({"msg": "error", "player_id": player.Id, "error_message": "This cell has already been hit."}) + "\n"
        player.conn.send(rec_msg.encode("utf-8"))
        return
    other_player.conn.send(rec_msg.encode("utf-8"))

def game_hit_success(player, server, x, y):
    other_player = server.players.get(player.opponent_id)
    other_player.board[x][y] = "X"
    rec_msg = json.dumps({"msg": "game_hit_success", "player_id": player.Id, "x": x, "y": y}) + "\n"
    player.conn.send(rec_msg.encode("utf-8"))
    other_player.conn.send(rec_msg.encode("utf-8"))
    player.score += 1
    set_score(player, server, player.score)
    if player.score == SHIP_COUNT:
        # Player wins the game
        rec_msg = json.dumps({"msg": "game_over", "player_id": player.Id, "result": "win"}) + "\n"
        player.conn.send(rec_msg.encode("utf-8"))
        other_player.conn.send(rec_msg.encode("utf-8"))

def error(player,msg,server):

    pass
