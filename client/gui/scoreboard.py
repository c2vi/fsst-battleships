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

        self.layout_scoreboard = QGridLayout()
        self.layout_scoreboard.addWidget(self.scroll_area, 0, 0)
        self.layout_scoreboard.addWidget(self.button_game, 1, 1)
        self.layout_scoreboard.addWidget(self.button_scoreboard, 1, 2)
        self.layout_scoreboard.addWidget(self.button_playerlist, 1,3)

        self.setLayout(self.layout_scoreboard)

    def button_game_clicked(self):
        self.main.state = "game"
        self.main.game_state()

    def button_playerlist_clicked(self):
        self.main.state = "playerlist"
        self.main.game_state()
