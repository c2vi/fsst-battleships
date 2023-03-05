import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QApplication,
  QDialog,
  QMainWindow,
  QMessageBox,
  QPushButton,
  QLabel,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Screen")
        self.setFixedSize(1000, 800)

        txt = "test score : 25"  # placeholder, later set_score
        score = QLabel(txt)
        score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(score)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


