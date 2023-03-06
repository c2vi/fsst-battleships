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

    def __init__(self, main):
        super().__init__()
        self.main = main

        self.scroll_area = QScrollArea()
        self.state = "playerlist"

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

    def button_game_clicked(self):
        self.main.state = "game"

    def button_scoreboard_clicked(self):
        self.main.state = "scoreboard"

    def player_list(self, players):

        inside_widget = QWidget()
        inside_layout = QVBoxLayout()

        self.scroll_area.setLayout(inside_layout)

        self.scroll_area.setWidget(inside_widget)
        self.scroll_area.setWidgetResizable(True)
        for player in players:
            txt = players["name"]
            names_widget = QPushButton(txt)
            inside_layout.addWidget(names_widget)