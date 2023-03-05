import gui.main as gui
import sys
from PyQt6.QtWidgets import (QApplication)


class Client:
    def __init__(self):
        app = QApplication(sys.argv)
        window = gui.MainWindow(self)
        window.show()
        app.exec()

    def match_req(self, player_id):
        print(player_id)

    def set_name(self, name):
        print(name)


client = Client()
