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


class Scoreboard(QWidget):

    def __init__(self, main):
        super().__init__()

        self.main = main
        self.state = "scoreboard"

        self.scroll_area = QScrollArea()

        self.button_game = QPushButton("GAME")
        self.button_game.clicked.connect(self.button_game_clicked)
        self.button_scoreboard = QPushButton("SCOREBOARD")
        self.button_scoreboard.setEnabled(False)
        self.button_playerlist = QPushButton("PLAYERLIST")
        self.button_playerlist.clicked.connect(self.button_playerlist_clicked)

        self.layout_playerlist = QGridLayout()
        self.layout_playerlist.addWidget(self.scroll_area, 0, 0)
        self.layout_playerlist.addWidget(self.button_game, 1, 1)
        self.layout_playerlist.addWidget(self.button_scoreboard, 2, 1)
        self.layout_playerlist.addWidget(self.button_playerlist, 3, 1)

        self.setLayout(self.layout_playerlist)

    def button_game_clicked(self):
        self.main.state = "game"

    def button_playerlist_clicked(self):
        self.main.state = "playerlist"
