import json, os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class MessageHandler:
    def __init__(self, gui, client):
        self.gui = gui
        self.client = client
        self.commands  = {"player_list": self.player_list,
                          "match_req": self.match_req,
                          "match_req_cancel": self.match_req_cancel,
                          "match_deny": self.match_deny,
                          "game_start": self.game_start, 
                          "game_place_invalid": self.game_place_invalid,
                          "game_do_hit": self.game_do_hit,
                          "game_hit_success": self.game_hit_success,
                          "set_score": self.set_score,
                          "game_over": self.game_over,
                          "error": self.error}
    

    def player_list(self, msg):
        player_list = msg["players"]
        self.gui.player_list(player_list)

    def match_req(self, msg):
        self.gui.match_req(msg["player_id"])

    def match_deny(self, msg):
        self.gui.match_deny()

    def match_req_cancel(self,msg):
        player_id = msg["player_id"]
        self.gui.match_req_cancel()

    def game_start(self,msg):
        self.gui.game_start()

    def game_over(self, msg):
        self.gui.game_over(msg)

    def game_place_invalid(self,msg):
        pass 
        # TODO
        self.gui.game_place_invalid()

    def game_do_hit(self,msg):
        pass
        #TODO
        self.gui.game_do_hit()

    def game_hit(self, msg):
        x = msg["x"] 
        y = msg["y"]
        self.gui.game_hit(x, y)

    def game_hit_success(self,msg):
        x = msg["x"] 
        y = msg["y"]
        self.gui.game_hit_success(x, y)

    def set_score(self,msg):
        score = msg["score"]
        self.gui.set_score()

    def error(self,msg):
        err_msg = msg["err_msg"]
        self.gui.error()
        
    def wrong_commands(self,msg):
        print("Command not found!", msg)

    def handle_msg(self,message):
        handler = self.commands.get(message["msg"] ,self.wrong_commands) #Checks if the function is there and executes them if yes
        self.client.signal.emit((handler, message))
        

