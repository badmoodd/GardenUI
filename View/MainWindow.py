# This Python file uses the following encoding: utf-8
import json
from pathlib import Path
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QPushButton

from Controller.ApplicationController import ApplicationController

WIDTH = 4
HEIGHT = 5
PATH_TO_PLANTS = "Resorces/new_storage.json"


def button2_clicked():
    print("Button 2 clicked")


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        self.cells_buttons_list = self.fill_cells_with_images()
        self.cells_buttons_list[0].clicked.connect(button2_clicked)

    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "UI/main_window.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def kal(self):
        main = []

        for i in range(WIDTH):
            for j in range(HEIGHT):
                r = []
                stri = "cell" + str(i) + str(j)

                button = self.findChild(QPushButton, stri)
                button.setStyleSheet("border-image : url(Resorces/assets/weed.png);")
                r.append(button)
            main.append(r)

        return main

    def fill_cells_with_images(self):
        entities: dict = ApplicationController.read_entities_from(PATH_TO_PLANTS)
        cells: list = []

        for a_plot in entities["plots"]:
            button_name = "cell" + str(a_plot["width"]) + str(a_plot["height"])
            button = self.findChild(QPushButton, button_name)
            if a_plot["is_empty"]:
                cells.append(button)
                continue
            else:
                if not a_plot["plant"]["no_plant"]:
                    if a_plot["plant"]["name_of_plant"] == "potato":
                        button.setStyleSheet("border-image : url(Resorces/assets/potato.png);")
                        cells.append(button)
                        continue
                    if a_plot["plant"]["name_of_plant"] == "carrot":
                        button.setStyleSheet("border-image: url(Resorces/assets/carrot.png);")
                        cells.append(button)
                        continue
                    if a_plot["plant"]["name_of_plant"] == "tomato":
                        button.setStyleSheet("border-image : url(Resorces/assets/tomato.png);")
                        cells.append(button)
                        continue
                    if a_plot["plant"]["name_of_plant"] == "cucumber":
                        button.setStyleSheet("border-image : url(Resorces/assets/cucumber.png);")
                        cells.append(button)
                        continue
                    if a_plot["plant"]["name_of_plant"] == "zucchini":
                        button.setStyleSheet("border-image : url(Resorces/assets/zucchini.png);")
                        cells.append(button)
                        continue
                    if a_plot["plant"]["name_of_plant"] == "eggplant":
                        button.setStyleSheet("border-image: url(Resorces/assets/eggplant.png);")
                        cells.append(button)
                        continue
                if not a_plot["osot"]["no_osot"]:
                    button.setStyleSheet("border-image : url(Resorces/assets/weed.png);")
                    cells.append(button)
        return cells
