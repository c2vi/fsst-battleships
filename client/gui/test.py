import sys
from PyQt6.QtWidgets import (
  QApplication,
  QDialog,
  QMainWindow,
  QMessageBox,
  QPushButton,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Screen")
        self.setFixedSize(1000, 800)

        def button_clicked(self):
              mtch_rqst = QMessageBox(self)
              mtch_rqst.setWindowTitle("Match Request")
              txt = "... requests a match!\n Play ...?"  # later err-msg
              mtch_rqst.setText(txt)
              mtch_rqst.setStandardButtons(
                  QMessageBox.StandardButton.Yes
                  | QMessageBox.StandardButton.No)
              mtch_rqst.setStyleSheet("QLabel{min-width:300 px; font-size: 24px;} QPushButton{ width:100px; font-size: 14px; }")
              button = mtch_rqst.exec()
              # Look up the button enum entry for the result.
              button = QMessageBox.StandardButton(button)
              if button == QMessageBox.StandardButton.Yes:
                # message needs to be send!
                print("Yes")
              else:
                print("No")
        button_clicked(self)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


