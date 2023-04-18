# This Python file uses the following encoding: utf-8
import sys

from PySide6 import QtWidgets
from View.MainWindow import Ui_main_screen
from Model.garden import Garden, Plant, Carrot, Weed, Zucchini

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    garden = Garden()
    garden.set_plant(Zucchini(), 2, 4)
    main_screen = QtWidgets.QWidget()
    ui = Ui_main_screen()

    ui.setupUi(main_screen)
    main_screen.show()
    sys.exit(app.exec())
