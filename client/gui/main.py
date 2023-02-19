import sys
import matchmaking
from PyQt6.QtWidgets import (
  QApplication,
  QGridLayout,
  QMainWindow,
  QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        self.setWindowTitle("Main Screen")
        self.setFixedSize(1000, 800)
        tesr = matchmaking.matchmaking()
        layout.addWidget(tesr, 0, 0)

        WrapperWidget = QWidget()
        WrapperWidget.setLayout(layout)
        self.setCentralWidget(WrapperWidget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
