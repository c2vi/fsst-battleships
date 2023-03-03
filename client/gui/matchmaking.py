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


class Matchmaking(QWidget):
    def player_list(self):

        inside_widget = QWidget()
        inside_layout = QVBoxLayout

        self.scroll_area.setWidget(inside_widget)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area.setLayout(inside_layout) # help


        players = {"name": "THOMML"}

        for player in players:
            txt = "THOMML"
            print(player)
            names_widget = QPushButton(txt)
            inside_layout.addWidget(names_widget)

    def __init__(self, client=None):
        super().__init__()
        self.client = client
        self.button = QPushButton("Done")
        self.scroll_area = QScrollArea()


        # define label widget + set font + center label
        widget_nme_lbl = QLabel("Name")
        font = widget_nme_lbl.font()
        font.setPointSize(30)
        widget_nme_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # define line widget where user can enter name
        widget_lne_nme = QLineEdit()
        widget_lne_nme.setMaxLength(10)

        self.layout_mtchmkng = QGridLayout()
        self.layout_mtchmkng.addWidget(widget_nme_lbl, 0, 0)
        self.layout_mtchmkng.addWidget(widget_lne_nme, 0, 1)
        self.layout_mtchmkng.addWidget(self.button, 0, 2)
        self.layout_mtchmkng.addWidget(self.scroll_area, 1, 1)

        self.setLayout(self.layout_mtchmkng)
        self.player_list()

    def button_clicked(self):
        print("START GAME")
        self.client.set_name()


