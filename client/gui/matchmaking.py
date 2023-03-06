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

    def player_list(self, players=[]):

        #inside_layout = self.scroll_area.layout()

        #for i in reversed(range(layout.count())): 
            #layout.itemAt(i).widget().setParent(None)

        inside_widget = QWidget()
        inside_layout = QVBoxLayout()
        inside_widget.setLayout(inside_layout)

        self.scroll_area.setWidget(inside_widget)
        self.scroll_area.setWidgetResizable(True)

        for player in players:
            txt = player["name"]
            player_id = player["id"]
            print(player)
            names_widget = QPushButton(txt)
            names_widget.clicked.connect(self.name_clicked(player_id))
            inside_layout.addWidget(names_widget)

        #self.clear_item(self.scroll_area)
        #self.scroll_area.setLayout(inside_layout)

    def name_clicked(self, player_id):
        def inner():
            print("test worked")
            self.client.match_req(player_id)

        return inner

    def __init__(self, client=None):
        super().__init__()

        # define line widget where user can enter name
        self.widget_lne_nme = QLineEdit()
        self.widget_lne_nme.setMaxLength(10)

        self.client = client
        self.button = QPushButton("Done")
        self.button.clicked.connect(self.button_clicked)
        self.scroll_area = QScrollArea()


        # define label widget + set font + center label
        widget_nme_lbl = QLabel("Name")
        font = widget_nme_lbl.font()
        font.setPointSize(30)
        widget_nme_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)



        self.layout_mtchmkng = QGridLayout()
        self.layout_mtchmkng.addWidget(widget_nme_lbl, 0, 0)
        self.layout_mtchmkng.addWidget(self.widget_lne_nme, 0, 1)
        self.layout_mtchmkng.addWidget(self.button, 0, 2)
        self.layout_mtchmkng.addWidget(self.scroll_area, 1, 1)

        self.setLayout(self.layout_mtchmkng)
        self.player_list()

    def button_clicked(self):
        print("START GAME")
        name = self.widget_lne_nme.text()
        self.client.set_name(name)


