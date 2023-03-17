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


class PlaceShips(QWidget):
    def __init__(self, main):
        super().__init__()

        self.main = main
        self.main.state = "place-ships"

        self.button_game = QPushButton("GAME")
        self.button_game.setEnabled(False)
        self.button_scoreboard = QPushButton("SCOREBOARD")
        self.button_scoreboard.clicked.connect(self.button_scoreboard_clicked)
        self.button_playerlist = QPushButton("PLAYERLIST")
        self.button_playerlist.clicked.connect(self.button_playerlist_clicked)

        enemy_field_layout = QGridLayout()

        own_field_layout = QGridLayout()

        for x in range(1, 13):
            for y in range(1, 13):
                own_field_button = QPushButton()
                own_field_button.clicked.connect(self.own_button_clicked(own_field_button))
                own_field_layout.addWidget(own_field_button, x, y)

        own_field_widget = QWidget()
        own_field_widget.setLayout(own_field_layout)

        game_layout = QGridLayout()
        game_layout.addWidget(own_field_widget, 0, 0)
        game_layout.addWidget(self.button_game, 1, 1)
        game_layout.addWidget(self.button_scoreboard, 1, 2)
        game_layout.addWidget(self.button_playerlist, 1, 3)

        self.setLayout(game_layout)

    def button_playerlist_clicked(self):
        self.main.state = "playerlist"

    def button_scoreboard_clicked(self):
        self.main.state = "scoreboard"

    def own_button_clicked(self, own_field_button):
        def inner():
            own_field_button.setStyleSheet("background-color:red")
        return inner
