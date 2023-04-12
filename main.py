# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication
from View.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
