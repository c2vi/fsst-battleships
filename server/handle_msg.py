import json
SHIP_COUNT = 10

def set_name(player,msg,server):
    player.player_name = msg["name"]

    msg = (json.dumps({"msg": "player_list", "players": server.get_players()}) + "\n")
    for player in server.players.values():
        player.conn.send((msg + "").encode("utf-8"))

def match_req_cancel(player,msg,server):
    rec_msg = json.dumps({"msg": "match_req_cancel", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_id"])
    other_player.conn.send(rec_msg.encode("utf-8"))

def match_ack(player,msg,server):
    other_player = server.players.get(msg["player_id"])
    # TODO: set opponent_id of player and other_player
    rec_msg = json.dumps({"msg": "game_start", "player_id" : player.Id, "other_player_id" : other_player.Id}) + "\n"

    other_player.conn.send(rec_msg.encode("utf-8"))
    player.conn.send(rec_msg.encode("utf-8"))

def match_req(player,msg,server):
    other_player = server.players[msg["player_id"]]
    msg["player_id"] = player.Id
    other_player.conn.send(json.dumps(msg).encode("utf-8") + b"\n")

def match_deny(player,msg,server):
    rec_msg = json.dumps({"msg": "match_deny", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_id"])
    other_player.conn.send(rec_msg.encode("utf-8"))

def game_cancel(player,msg,server):
    rec_msg = json.dumps({"msg": "game_cancel", "player_id": player.Id}) + "\n"
    other_player = server.players.get(msg["player_id"])
    other_player.conn.send(rec_msg.encode("utf-8"))

def game_place(player,msg,server):
    # TODO:
    # - set player.has_placed to true
    # - if the other player in that game has already placed his ships, then send a game_do_hit to player
    # - you can get the other player by: server.players[player.opponent_id]

def game_hit(player,msg,server):
    x = msg["x"]
    y = msg["y"]
    other_player = server.players.get(player.opponent_id)
    cell_value = other_player.board[x][y]
    if cell_value == " ":
        # Missed
        other_player.board[x][y] = "O"
        rec_msg = json.dumps({"msg": "game_hit_miss", "player_id": player.Id, "x": x, "y": y}) + "\n"
        # TODO: send game_do_hit to the other_player
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
            # TODO: send a message with result: "lose" to the other_player
            other_player.conn.send(rec_msg.encode("utf-8"))
            return
        else:
            # TODO: send game_do_hit to the this player, so that he can do another hit.
            # replace the pass with some code
            pass
    else:
        # Already hit this cell
        rec_msg = json.dumps({"msg": "error", "player_id": player.Id, "error_message": "This cell has already been hit."}) + "\n"
        player.conn.send(rec_msg.encode("utf-8"))
        return

def error(player,msg,server):
    #TODO: print "ERROR: " and the msg
