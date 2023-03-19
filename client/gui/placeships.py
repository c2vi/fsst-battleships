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
        self.button_scoreboard.setEnabled(False)
        self.button_playerlist = QPushButton("PLAYERLIST")
        self.button_playerlist.setEnabled(False)
        self.button_done = QPushButton("DONE")
        self.button_done.clicked.connect(self.button_done_clicked)

        enemy_field_layout = QGridLayout()

        own_field_layout = QGridLayout()

        for x in range(1, 13):
            for y in range(1, 13):
                own_field_button = QPushButton()
                own_field_button.clicked.connect(self.own_button_clicked(own_field_button))
                own_field_layout.addWidget(own_field_button, x, y)

        own_field_widget = QWidget()
        own_field_widget.setLayout(own_field_layout)


        self.shiplayout = QGridLayout()
        self.Flugzeugträger_layout = QGridLayout()
        self.Zweierschiff_layout1 = QGridLayout()
        self.Zweierschiff_layout2 = QGridLayout()
        self.Zweierschiff_layout3 = QGridLayout()
        self.Dreierschiff_layout1 = QGridLayout()
        self.Dreierschiff_layout2 = QGridLayout()

        self.ships = QWidget()
        self.ships.setLayout(self.shiplayout)

        def Zweierschiff():
            shippiece1 = QPushButton()
            shippiece2 = QPushButton()

            DrehenZweierschiff = QPushButton("Rotate")

            shippiece1.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
            shippiece2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')

            Zweierschiffwidget = QWidget()
            Zweierschifflayout = QGridLayout()

            Zweierschifflayout.addWidget(DrehenZweierschiff,0,0)
            Zweierschifflayout.addWidget(shippiece1, 1, 0)
            Zweierschifflayout.addWidget(shippiece2, 2, 0)

            Zweierschiffwidget.setLayout(Zweierschifflayout)

            return Zweierschiffwidget

        def Flugzeugträger():
            shippiece1 = QPushButton()
            shippiece2 = QPushButton()
            shippiece3 = QPushButton()
            shippiece4 = QPushButton()

            DrehenFlugzeugträger = QPushButton("Rotate")

            shippiece1.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
            shippiece2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
            shippiece3.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
            shippiece4.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')


            Flugzeugträgerwidget = QWidget()
            Flugzeugträgerlayout = QGridLayout()

            Flugzeugträgerlayout.addWidget(DrehenFlugzeugträger,0,0)
            Flugzeugträgerlayout.addWidget(shippiece1, 1, 0)
            Flugzeugträgerlayout.addWidget(shippiece2, 2, 0)
            Flugzeugträgerlayout.addWidget(shippiece3, 2, 1)
            Flugzeugträgerlayout.addWidget(shippiece4, 3, 1)

            Flugzeugträgerwidget.setLayout(Flugzeugträgerlayout)

            return Flugzeugträgerwidget

        def Dreierschiff():
            shippiece1 = QPushButton()
            shippiece2 = QPushButton()
            shippiece3 = QPushButton()

            DrehenDreierschiff = QPushButton("Rotate")


            shippiece1.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
            shippiece2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
            shippiece3.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')

            Dreierschiffwidget = QWidget()
            Dreierschifflayout = QGridLayout()

            Dreierschifflayout.addWidget(DrehenDreierschiff, 0, 0)
            Dreierschifflayout.addWidget(shippiece1, 1, 0)
            Dreierschifflayout.addWidget(shippiece2, 2, 0)
            Dreierschifflayout.addWidget(shippiece3, 3, 0)

            Dreierschiffwidget.setLayout(Dreierschifflayout)
            return Dreierschiffwidget

        self.shiplayout.addWidget(Flugzeugträger(), 1, 0)
        self.shiplayout.addWidget(Zweierschiff(), 1, 2)
        self.shiplayout.addWidget(Zweierschiff(), 1, 3)
        self.shiplayout.addWidget(Zweierschiff(), 1, 4)
        self.shiplayout.addWidget(Dreierschiff(), 6, 1)
        self.shiplayout.addWidget(Dreierschiff(), 6, 2)










        game_layout = QGridLayout()
        game_layout.addWidget(own_field_widget, 0, 0)
        game_layout.addWidget(self.button_game, 1, 1)
        game_layout.addWidget(self.button_scoreboard, 1, 2)
        game_layout.addWidget(self.button_playerlist, 1, 3)
        game_layout.addWidget(self.button_done, 1, 0)
        game_layout.addWidget(self.ships, 0, 1)

        self.setLayout(game_layout)

    def button_playerlist_clicked(self):
        self.main.state = "playerlist"
        self.main.game_state()

    def button_scoreboard_clicked(self):
        self.main.state = "scoreboard"
        self.main.game_state()

    def button_done_clicked(self):
        self.main.state = "game"
        # you need to parse an array with the coordinates of the ships, if you don't the client crashes!
        self.main.client.game_place()

    def own_button_clicked(self, own_field_button):
        def inner():
            own_field_button.setStyleSheet("background-color:red")
        return inner


