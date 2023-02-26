class MessageHandler:
    def __init__(self):
        self.commands  = {"player_list": player_list,
                          "match_req": match_req,
                          "match_req_cancel": match_req_cancel,
                          "game_start": game_start, 
                          "game_place_invalid": game_place_invalid,
                          "game_do_hit": game_do_hit,
                          "game_hit_success": game_hit_success,
                          "set_score": set_score,
                          "error": error}
        

def player_list(self,msg):
    player_list = msg["players"]

def match_req(self,msg):
    player_id = msg["player_id"]

def match_req_cancel(self,msg):
    player_id = msg["player_id"]

def game_start(self,msg):
    boats = msg["boats"]
    grid_size_x = msg["grid_size_x"]
    grid_size_y = msg["grid_size_y"]

def game_place_invalid(self,msg):
    pass 
    # TODO
def game_do_hit(self,msg):
    pass
    #TODO
def game_hit_success(self,msg):
    x = msg["x"]
    y = msg["y"]

def set_score(self.msg):
    score = msg["score"]

def error(self,msg):
    err_msg = msg["err_msg"]
    
def wrong_commands(self,msg):
    print("Command not found!")

def handle_msg(self,message):
    for msg in message:
            self.commands.get(msg,wrong_commands)(message[msg]) #Checks if the function is there and executes them if yes 
    