import handle_msg
import json


def send_server( message):
    import main_network
    json_message = json.dumps(message)
    main_network.Network.socket.send(str(json_message).encode("utf-8"))
    


def set_name( name):

    dic = {
        "msg":"set_name",
        "name": name
    }
    send_server(dic)

def match_req( player_id):
    dic = {
        "msg":"match_req",
        "player_id": player_id
    }
    send_server(dic)

def match_ack( player_id):
    dic = {
        "msg":"match_ack",
        "player_id" : player_id
    }
    send_server(dic)

def match_deny( player_id):
    dic = {
        "msg":"match_deny",
        "player_id" : player_id
    }
    send_server(dic)

def game_cancel():
    dic = {
        "msg":"game_cancel"
    }
    send_server(dic)

def game_place( ships):
    dic = {
        "msg":"game_cancel",
        "ships": ships
    }
    send_server(dic)

def game_hit( x,y):
    dic = {
        "msg":"game_hit",
        "x": x,
        "y": y}
    send_server(dic)
