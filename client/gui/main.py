import sys
import matchmaking
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QApplication,
  QGridLayout,
  QMainWindow,
  QWidget,
  QMessageBox,
  QLabel,
  QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.state = "matchmaking"

        layout = QGridLayout()
        self.setWindowTitle("Main Screen")
        self.setFixedSize(1000, 800)
        test = matchmaking.matchmaking()
        layout.addWidget(test, 0, 0)

        self.switch_button = QPushButton("SCOREBOARD")
        WrapperWidget = QWidget()
        WrapperWidget.setLayout(layout)
        self.setCentralWidget(WrapperWidget)
    def switch_view(self):
        if self.switch_button:
            self.state = "scoreboard"
    def player_list (self, players):
        for player in players:
            txt = players["name"]
            names_widget = QLabel(txt)




    def match_req(self):
        mtch_rqst = QMessageBox(self)
        mtch_rqst.setWindowTitle("Match Request")
        txt = "... requests a match!\n Play ...?"  # later match-request
        mtch_rqst.setText(txt)
        mtch_rqst.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No)
        mtch_rqst.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 24px;} QPushButton{ width:100px; font-size: 14px; }")
        button = mtch_rqst.exec()
        # Look up the button enum entry for the result.
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            # message needs to be send!
            print("Yes")
        else:
            print("No")
    match_req()


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
        txt = "test score : 25" # placeholder, later set_score
        score = QLabel(txt)
        score.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def error(self):
        #sets up the message box
        err_bx = QMessageBox(self)
        err_bx.setWindowTitle("Error Box")
        txt = "test"  # temp var - later err-msg
        err_bx.setText(txt)
        err_bx.setStandardButtons(QMessageBox.StandardButton.Ok)
        err_bx.setIcon(QMessageBox.Icon.Critical)
        #changes the size of the label => changes the size of the box
        err_bx.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 24px;} QPushButton{ width:100px; font-size: 14px; }")
        button = err_bx.exec()
        #happens after you press the OK button
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Ok:
            print("Ok!")
            self.centralWidget(self)

    error()




if __name__ == "__Main__":
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
