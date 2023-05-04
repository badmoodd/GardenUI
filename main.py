# This Python file uses the following encoding: utf-8
import sys

from PySide6 import QtWidgets
from View.MainWindow import Ui_main_screen
from Controller.ViewController import ViewController
from Model.garden import Garden

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_screen = QtWidgets.QWidget()
    ui = Ui_main_screen()
    ui.setupUi(main_screen, ViewController(Garden(), main_screen))

    # controller = ViewController(Garden(), main_screen)
    main_screen.show()
    sys.exit(app.exec())
