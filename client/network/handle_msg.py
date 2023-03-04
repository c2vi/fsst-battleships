import json, os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import client.main as gui

class MessageHandler:
    def __init__(self, gui:gui.MainWindow):
        self.gui = gui
        self.commands  = {"player_list": self.player_list,
                          "match_req": self.match_req,
                          "match_req_cancel": self.match_req_cancel,
                          "game_start": self.game_start, 
                          "game_place_invalid": self.game_place_invalid,
                          "game_do_hit": self.game_do_hit,
                          "game_hit_success": self.game_hit_success,
                          "set_score": self.set_score,
                          "error": self.error}
    
    def handle_message(self, message=any):
        message_dict = json.loads(message) #json string übergeben, krieg ein dict zurück

        message_dict["message_dict"]
        self.commands.get(message_dict,self.wrong_commands)(message_dict)
        

    def player_list(self,msg):
        player_list = msg["players"]
        self.gui.player_list(player_list)


    def match_req(self,msg):
        self.gui.match_req()

    def match_req_cancel(self,msg):
        player_id = msg["player_id"]
        self.gui.match_req_cance()

    def game_start(self,msg):
        boats = msg["boats"]
        grid_size_x = msg["grid_size_x"]
        grid_size_y = msg["grid_size_y"]
        self.gui.game_start()

    def game_place_invalid(self,msg):
        pass 
        # TODO
        self.gui.game_place_invalid()

    def game_do_hit(self,msg):
        pass
        #TODO
        self.gui.game_do_hit()

    def game_hit_success(self,msg):
        x = msg["x"] 
        y = msg["y"]
        self.gui.game_hit_success()

    def set_score(self,msg):
        score = msg["score"]
        self.gui.set_score()

    def error(self,msg):
        err_msg = msg["err_msg"]
        self.gui.error()
        
    def wrong_commands(self,msg):
        print("Command not found!")

    def handle_msg(self,message):
        for msg in message:
                self.commands.get(msg,self.wrong_commands)(message) #Checks if the function is there and executes them if yes 
        