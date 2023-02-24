import sys
import matchmaking
from PyQt6.QtWidgets import (
  QApplication,
  QGridLayout,
  QMainWindow,
  QWidget,
  QMessageBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        layout = QGridLayout()
        self.setWindowTitle("Main Screen")
        self.setFixedSize(1000, 800)
        test = matchmaking.matchmaking()
        layout.addWidget(test, 0, 0)

        WrapperWidget = QWidget()
        WrapperWidget.setLayout(layout)
        self.setCentralWidget(WrapperWidget)
    def player_list (self):
    def set_name (self):

    def match_req(self):

    def match_req_cancel(self):

    def match_ack(self):

    def match_deny(self):

    def game_start(self):

    def game_cancel(self):

    def game_place(self):

    def game_place_invalid(self):

    def game_do_hit(self):

    def game_hit(self):

    def game_hit_success(self):

    def set_score(self):

    def error(self):
        #set up the error message box
        err_bx = QMessageBox()
        err_bx.setWindowTitle("Error Box")
        txt = "test" #later err-msg
        err_bx.setText(txt)
        err_bx.setIcon(QMessageBox.Critical)
        err_bx.setStandardButtons(QMessageBox.Ok)
        err_bx.buttonClicked.connect(self.popup_clicked)
        #shows error message box
        #err_bx.exec_()

        def popup_clicked(self, i):
            print(i.text())





app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
