
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QGridLayout,
  QWidget,
  QLineEdit,
  QLabel,
  QPushButton,
)



class matchmaking(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Done")

        # define label widget + set font + center label
        widget_nme_lbl = QLabel("Name")
        font = widget_nme_lbl.font()
        font.setPointSize(30)
        widget_nme_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #define line widget where user can enter name
        widget_lne_nme = QLineEdit()
        widget_lne_nme.setMaxLength(10)

        layout_mtchmkng = QGridLayout()
        layout_mtchmkng.addWidget(widget_nme_lbl, 0, 0)
        layout_mtchmkng.addWidget(widget_lne_nme, 0, 1)
        layout_mtchmkng.addWidget(self.button, 1, 0)

        self.setLayout(layout_mtchmkng)
    def button_clicked(self):
        set_name()