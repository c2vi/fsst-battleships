import sys
from .matchmaking import Matchmaking
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
    def __init__(self, client=None):
        super().__init__()
        self.client = client
        self.state = "matchmaking"

        # connect to signal from client class, because qt gui can't be updated from a different thread
        self.client.signal.connect(self.signal_handler)


        layout = QGridLayout()
        self.setWindowTitle("Main Screen")
        self.setFixedSize(1000, 800)
        self.matchmaking = Matchmaking(client)
        layout.addWidget(self.matchmaking, 0, 0)

        self.switch_button = QPushButton("SCOREBOARD")
        if self.state == "scoreboard":
            self.switch_button.setText("GAME")
        else:
            self.switch_button.setText("SCOREBOARD")
        WrapperWidget = QWidget()
        WrapperWidget.setLayout(layout)
        self.setCentralWidget(WrapperWidget)

    def signal_handler(self, duple):
        hanlder = duple[0]
        message = duple[1]
        print("in handler", message)
        hanlder(message)

    def player_list (self, players):
        if self.state == "playerlist":
            print("playerlist function from player list")
        if self.state == "matchmaking":
            print("playerlist function from matchmaking")
            self.matchmaking.player_list(players)

    def match_req(self, player_id):
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

    def match_req_cancel(self):
        pass

    def match_ack(self):
        pass

    def match_deny(self):
        pass

    def game_start(self):
        pass

    def game_cancel(self):
        pass

    def game_place(self):
        pass

    def game_place_invalid(self):
        pass

    def game_do_hit(self):
        pass

    def game_hit(self):
        pass

    def game_hit_success(self):
        pass

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


if __name__ == "__Main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
