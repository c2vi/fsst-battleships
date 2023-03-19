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
        self.selected_ship = None
        self.selected_x = None
        self.selected_y = None
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
        self.own_field_Buttons = []
        for x in range(1, 13):
            for y in range(1, 13):
                own_field_button = QPushButton()
                own_field_layout.addWidget(own_field_button, x, y)
                own_field_button.clicked.connect(self.place_ship(x,y))
                own_field_button.x = x
                own_field_button.y = y


                self.own_field_Buttons.append(own_field_button)

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



        self.ship_map_flug = [
            ["X"," "," "," "," "," "," "],
            ["X","X"," "," "," "," "," "],
            [" ","X"," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
        ]
        self.ship_map_zweier = [
            ["X"," "," "," "," "," "," "],
            ["X"," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
        ]
        self.ship_map_dreier = [
            ["X", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
        ]

        self.shiplayout.addWidget(self.make_ship(self.ship_map_flug), 1, 0)
        self.shiplayout.addWidget(self.make_ship(self.ship_map_zweier), 1, 2)
        self.shiplayout.addWidget(self.make_ship(self.ship_map_zweier), 1, 3)
        self.shiplayout.addWidget(self.make_ship(self.ship_map_zweier), 1, 4)
        self.shiplayout.addWidget(self.make_ship(self.ship_map_dreier), 6, 1)
        self.shiplayout.addWidget(self.make_ship(self.ship_map_dreier), 6, 2)











        game_layout = QGridLayout()
        game_layout.addWidget(own_field_widget, 0, 0)
        game_layout.addWidget(self.button_game, 1, 1)
        game_layout.addWidget(self.button_scoreboard, 1, 2)
        game_layout.addWidget(self.button_playerlist, 1, 3)
        game_layout.addWidget(self.button_done, 1, 0)
        game_layout.addWidget(self.ships, 0, 1)

        self.setLayout(game_layout)

    def Offset(self, ship, y, x):
        def Inner():
            print("Offset",ship.map)
            self.selected_ship = ship
            self.selected_x = x
            self.selected_y = y

        return Inner

    def make_ship(self, ship_map):
        ship = QWidget()
        ship_layout = QGridLayout()
        ship.map = ship_map

        for x in range(0, 6):
            for y in range(0, 6):
                ship_piece = QPushButton()
                if ship_map[y][x] == "X":

                    ship_layout.addWidget(ship_piece, y, x)
                    ship_piece.clicked.connect(self.Offset(ship, y, x))

        ship.setLayout(ship_layout)

        return ship

    def place_ship(self,x,y):

        def inner():
            absolut_x = x - self.selected_x
            absolut_y = y - self.selected_y
            self.selected_ship.setParent(None)
            for posx in range(0, 6):
                for posy in range(0, 6):

                    new_x = absolut_x + posx
                    new_y = absolut_y + posy

                    print(self.selected_ship.map,posx,posy)

                    if self.selected_ship.map[posx][posy] == "X":
                        print("if selected")
                        self.main.placeships_array[posx][posy] = "X"
                        for Button in self.own_field_Buttons:
                            print("for Button")
                            if new_x == Button.x and new_y == Button.y:
                                Button.setStyleSheet("background-color:blue")



            self.selected_ship = None
        return inner

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


