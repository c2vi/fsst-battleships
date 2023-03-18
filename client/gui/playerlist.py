from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QGridLayout,
  QWidget,
  QLineEdit,
  QLabel,
  QPushButton,
  QScrollArea,
  QVBoxLayout,
)


class Playerlist(QWidget):

    def __init__(self, main, client):
        super().__init__()
        self.main = main
        self.main.state = "playerlist"
        self.client = client

        self.scroll_area = QScrollArea()

        self.button_game = QPushButton("GAME")
        self.button_game.clicked.connect(self.button_game_clicked)
        self.button_scoreboard = QPushButton("SCOREBOARD")
        self.button_scoreboard.clicked.connect(self.button_scoreboard_clicked)
        self.button_playerlist = QPushButton("PLAYERLIST")
        self.button_playerlist.setEnabled(False)

        self.layout_playerlist = QGridLayout()
        self.layout_playerlist.addWidget(self.scroll_area, 0, 0)
        self.layout_playerlist.addWidget(self.button_game, 1, 1)
        self.layout_playerlist.addWidget(self.button_scoreboard, 2, 1)
        self.layout_playerlist.addWidget(self.button_playerlist, 3, 1)

        self.setLayout(self.layout_playerlist)
        self.player_list()

    def button_game_clicked(self):
        self.main.state = "game"
        self.main.game_state()

    def button_scoreboard_clicked(self):
        self.main.state = "scoreboard"
        self.main.game_state()

    def player_list(self, players=[]):

        inside_widget = QWidget()
        inside_layout = QVBoxLayout()
        inside_widget.setLayout(inside_layout)

        self.scroll_area.setWidget(inside_widget)
        self.scroll_area.setWidgetResizable(True)

        for player in self.main.players:
            txt = player["name"]
            player_id = player["id"]
            names_widget = QPushButton(txt)
            names_widget.clicked.connect(self.name_clicked(player_id, names_widget))
            inside_layout.addWidget(names_widget)

    def name_clicked(self, player_id, names_widget):
        def inner():
            self.client.match_req(player_id)
            names_widget.setEnabled(False)

        return inner
