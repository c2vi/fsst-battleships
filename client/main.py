import gui.main as gui
import sys
from PyQt6.QtWidgets import (QApplication)


class Client:
    def __init__(self):
        app = QApplication(sys.argv)
        window = gui.MainWindow(self)
        window.show()
        app.exec()


client = Client()
