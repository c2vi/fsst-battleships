import sys
from .game import  Game
from .playerlist import  Playerlist
from .scoreboard import  Scoreboard
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
        self.matchmaking = Matchmaking(client)

        # connect to signal from client class, because qt gui can't be updated from a different thread
        self.client.signal.connect(self.signal_handler)

        self.wrapper_layout = QGridLayout()
        self.setWindowTitle("Main Screen")
        self.setFixedSize(1000, 800)

        self.game_widget = Game(self)
        self.scoreboard_widget = Scoreboard(self)
        self.playerlist_widget = Playerlist(self)

        WrapperWidget = QWidget()
        WrapperWidget.setLayout(self.wrapper_layout)
        self.setCentralWidget(WrapperWidget)

        self.game_state()

    def signal_handler(self, duple):
        hanlder = duple[0]
        message = duple[1]
        hanlder(message)

    def game_state(self):
        if self.state == "game":
            Game(self)
            self.wrapper_layout.addWidget(self.game_widget, 0, 0)
        if self.state == "playerlist":
            Playerlist(self)
            self.wrapper_layout.addWidget(self.playerlist_widget, 0, 0)
        if self.state == "scoreboard":
            Scoreboard(self)
            self.wrapper_layout.addWidget(self.scoreboard_widget, 0, 0)
        if self.state == "matchmaking":
            self.wrapper_layout.addWidget(self.matchmaking, 0, 0)

    def player_list(self, players):
        if self.state == "playerlist":
            pass
            #print("playerlist function from player list")
        if self.state == "matchmaking":
            #print("playerlist function from matchmaking")
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
        match_request_cancel_box = QMessageBox(self)
        match_request_cancel_box.setWindowTitle("Match Request Cancel")
        txt = "press button to cancel match"  # later match-request
        match_request_cancel_box.setText(txt)
        match_request_cancel_box.setStandardButtons(QMessageBox.StandardButton.Cancel)
        match_request_cancel_box.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 24px;} QPushButton{ width:100px; font-size: 14px; }")

        button = match_request_cancel_box.exec()

        button = QMessageBox.StandardButton(button)

        if button == QMessageBox.StandardButton.Cancel:
            print("game canceled")
            txt_2 = "game canceled"
            match_request_cancel_box.setText(txt_2)

    def match_ack(self):
        self.state = "game"

    def match_deny(self):
        match_deny_box = QMessageBox(self)
        match_deny_box.setWindowTitle("Match deny")
        txt = "match denied"  # later match-request
        match_deny_box.setText(txt)
        match_deny_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        match_deny_box.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 24px;} QPushButton{ width:100px; font-size: 14px; }")

        button = match_deny_box.exec()

        button = QMessageBox.StandardButton(button)

        if button == QMessageBox.StandardButton.Ok:
            print("game denied")
            self.state = "matchmaking"

    def game_start(self):
        self.state = "game"

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
