# This Python file uses the following encoding: utf-8

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QPushButton

from Controller.ApplicationController import ApplicationController
from Controller.ViewController import ViewController
from View.EntityWindow import Ui_entity_screen
from Model.garden import Garden

WIDTH = 4
HEIGHT = 5
PATH_TO_PLANTS = "Resources/new_storage.json"


class Ui_main_screen(QtWidgets.QWidget):
    def setupUi(self, main_screen, controller):
        self.controller = controller
        main_screen.setObjectName("main_screen")
        main_screen.setEnabled(True)
        main_screen.resize(1000, 455)
        self.cell00 = QtWidgets.QPushButton(parent=main_screen)
        self.cell00.setGeometry(QtCore.QRect(30, 30, 71, 71))
        self.cell00.setStyleSheet("")
        self.cell00.setText("")
        self.cell00.setObjectName("cell00")
        self.cell00.clicked.connect(self.open_entity_window)

        self.cell01 = QtWidgets.QPushButton(parent=main_screen)
        self.cell01.setGeometry(QtCore.QRect(120, 30, 71, 71))
        self.cell01.setStyleSheet("")
        self.cell01.setText("")
        self.cell01.setObjectName("cell01")
        self.cell01.clicked.connect(self.open_entity_window)

        self.cell02 = QtWidgets.QPushButton(parent=main_screen)
        self.cell02.setGeometry(QtCore.QRect(210, 30, 71, 71))
        self.cell02.setStyleSheet("")
        self.cell02.setText("")
        self.cell02.setObjectName("cell02")
        self.cell02.clicked.connect(self.open_entity_window)

        self.cell03 = QtWidgets.QPushButton(parent=main_screen)
        self.cell03.setGeometry(QtCore.QRect(300, 30, 71, 71))
        self.cell03.setStyleSheet("")
        self.cell03.setText("")
        self.cell03.setObjectName("cell03")
        self.cell03.clicked.connect(self.open_entity_window)

        self.cell04 = QtWidgets.QPushButton(parent=main_screen)
        self.cell04.setGeometry(QtCore.QRect(390, 30, 71, 71))
        self.cell04.setStyleSheet("")
        self.cell04.setText("")
        self.cell04.setObjectName("cell04")
        self.cell04.clicked.connect(self.open_entity_window)

        self.cell14 = QtWidgets.QPushButton(parent=main_screen)
        self.cell14.setGeometry(QtCore.QRect(390, 120, 71, 71))
        self.cell14.setStyleSheet("")
        self.cell14.setText("")
        self.cell14.setObjectName("cell14")
        self.cell14.clicked.connect(self.open_entity_window)

        self.cell10 = QtWidgets.QPushButton(parent=main_screen)
        self.cell10.setGeometry(QtCore.QRect(30, 120, 71, 71))
        self.cell10.setStyleSheet("")
        self.cell10.setText("")
        self.cell10.setObjectName("cell10")
        self.cell10.clicked.connect(self.open_entity_window)

        self.cell12 = QtWidgets.QPushButton(parent=main_screen)
        self.cell12.setGeometry(QtCore.QRect(210, 120, 71, 71))
        self.cell12.setStyleSheet("")
        self.cell12.setText("")
        self.cell12.setObjectName("cell12")
        self.cell12.clicked.connect(self.open_entity_window)

        self.cell11 = QtWidgets.QPushButton(parent=main_screen)
        self.cell11.setGeometry(QtCore.QRect(120, 120, 71, 71))
        self.cell11.setStyleSheet("")
        self.cell11.setText("")
        self.cell11.setObjectName("cell11")
        self.cell11.clicked.connect(self.open_entity_window)

        self.cell13 = QtWidgets.QPushButton(parent=main_screen)
        self.cell13.setGeometry(QtCore.QRect(300, 120, 71, 71))
        self.cell13.setStyleSheet("")
        self.cell13.setText("")
        self.cell13.setObjectName("cell13")
        self.cell13.clicked.connect(self.open_entity_window)

        self.cell24 = QtWidgets.QPushButton(parent=main_screen)
        self.cell24.setGeometry(QtCore.QRect(390, 210, 71, 71))
        self.cell24.setStyleSheet("")
        self.cell24.setText("")
        self.cell24.setObjectName("cell24")
        self.cell24.clicked.connect(self.open_entity_window)

        self.cell20 = QtWidgets.QPushButton(parent=main_screen)
        self.cell20.setGeometry(QtCore.QRect(30, 210, 71, 71))
        self.cell20.setStyleSheet("")
        self.cell20.setText("")
        self.cell20.setObjectName("cell20")
        self.cell20.clicked.connect(self.open_entity_window)

        self.cell22 = QtWidgets.QPushButton(parent=main_screen)
        self.cell22.setGeometry(QtCore.QRect(210, 210, 71, 71))
        self.cell22.setStyleSheet("")
        self.cell22.setText("")
        self.cell22.setObjectName("cell22")
        self.cell22.clicked.connect(self.open_entity_window)

        self.cell21 = QtWidgets.QPushButton(parent=main_screen)
        self.cell21.setGeometry(QtCore.QRect(120, 210, 71, 71))
        self.cell21.setStyleSheet("")
        self.cell21.setText("")
        self.cell21.setObjectName("cell21")
        self.cell21.clicked.connect(self.open_entity_window)

        self.cell23 = QtWidgets.QPushButton(parent=main_screen)
        self.cell23.setGeometry(QtCore.QRect(300, 210, 71, 71))
        self.cell23.setStyleSheet("")
        self.cell23.setText("")
        self.cell23.setObjectName("cell23")
        self.cell23.clicked.connect(self.open_entity_window)

        self.cell34 = QtWidgets.QPushButton(parent=main_screen)
        self.cell34.setGeometry(QtCore.QRect(390, 300, 71, 71))
        self.cell34.setStyleSheet("")
        self.cell34.setText("")
        self.cell34.setObjectName("cell34")
        self.cell34.clicked.connect(self.open_entity_window)

        self.cell30 = QtWidgets.QPushButton(parent=main_screen)
        self.cell30.setGeometry(QtCore.QRect(30, 300, 71, 71))
        self.cell30.setStyleSheet("")
        self.cell30.setText("")
        self.cell30.setObjectName("cell30")
        self.cell30.clicked.connect(self.open_entity_window)

        self.cell32 = QtWidgets.QPushButton(parent=main_screen)
        self.cell32.setGeometry(QtCore.QRect(210, 300, 71, 71))
        self.cell32.setStyleSheet("")
        self.cell32.setText("")
        self.cell32.setObjectName("cell32")
        self.cell32.clicked.connect(self.open_entity_window)

        self.cell31 = QtWidgets.QPushButton(parent=main_screen)
        self.cell31.setGeometry(QtCore.QRect(120, 300, 71, 71))
        self.cell31.setStyleSheet("")
        self.cell31.setText("")
        self.cell31.setObjectName("cell31")
        self.cell31.clicked.connect(self.open_entity_window)

        self.cell33 = QtWidgets.QPushButton(parent=main_screen)
        self.cell33.setGeometry(QtCore.QRect(300, 300, 71, 71))
        self.cell33.setStyleSheet("")
        self.cell33.setText("")
        self.cell33.setObjectName("cell33")
        self.cell33.clicked.connect(self.open_entity_window)

        self.rain_button = QtWidgets.QPushButton(parent=main_screen)
        self.rain_button.setGeometry(QtCore.QRect(30, 400, 100, 32))
        self.rain_button.setObjectName("rain_button")
        self.rain_button.clicked.connect(lambda: controller.rain_call())

        self.drought_button = QtWidgets.QPushButton(parent=main_screen)
        self.drought_button.setGeometry(QtCore.QRect(160, 400, 100, 32))
        self.drought_button.setObjectName("drought_button")
        self.drought_button.clicked.connect(lambda: controller.drought_call())
        self.drought_button.clicked.connect(lambda: self.fill_cells_with_images())

        self.garden_image_button = QtWidgets.QPushButton(parent=main_screen)
        self.garden_image_button.setGeometry(QtCore.QRect(500, 30, 430, 350))
        self.garden_image_button.setText("")

        self.garden_image_button.setStyleSheet("border-image : url(Resources/assets/garden_image.png);")

        self.all_cells = [[self.cell00, self.cell01, self.cell02, self.cell03, self.cell04],
                          [self.cell10, self.cell11, self.cell12, self.cell13, self.cell14],
                          [self.cell20, self.cell21, self.cell22, self.cell23, self.cell24],
                          [self.cell30, self.cell31, self.cell32, self.cell33, self.cell34]]

        self.fill_cells_with_images()

        self.retranslateUi(main_screen)
        QtCore.QMetaObject.connectSlotsByName(main_screen)

    def retranslateUi(self, main_screen):
        _translate = QtCore.QCoreApplication.translate
        main_screen.setWindowTitle(_translate("main_screen", "Garden"))
        self.rain_button.setText(_translate("main_screen", "Rain"))
        self.drought_button.setText(_translate("main_screen", "Drought"))

    def fill_cells_with_images(self):
        entities: dict = ApplicationController.read_entities_from(PATH_TO_PLANTS)

        for a_plot in entities["plots"]:
            current_width = a_plot["width"]
            current_height = a_plot["height"]
            if a_plot["is_empty"]:
                self.get_cell_button(current_width, current_height). \
                    setStyleSheet("border-image : url(Resources/assets/garden_bed.png);")
                continue
            else:
                if not a_plot["plant"]["no_plant"]:
                    if a_plot["plant"]["name_of_plant"] == "potato":
                        self.get_cell_button(current_width, current_height). \
                            setStyleSheet("border-image : url(Resources/assets/potato.png);")
                        continue
                    if a_plot["plant"]["name_of_plant"] == "carrot":
                        self.get_cell_button(current_width, current_height). \
                            setStyleSheet("border-image : url(Resources/assets/carrot.png);")
                        continue
                    if a_plot["plant"]["name_of_plant"] == "tomato":
                        self.get_cell_button(current_width, current_height). \
                            setStyleSheet("border-image : url(Resources/assets/tomato.png);")
                        continue
                    if a_plot["plant"]["name_of_plant"] == "cucumber":
                        self.get_cell_button(current_width, current_height). \
                            setStyleSheet("border-image : url(Resources/assets/cucumber.png);")
                        continue
                    if a_plot["plant"]["name_of_plant"] == "zucchini":
                        self.get_cell_button(current_width, current_height). \
                            setStyleSheet("border-image : url(Resources/assets/zucchini.png);")
                        continue
                    if a_plot["plant"]["name_of_plant"] == "eggplant":
                        self.get_cell_button(current_width, current_height). \
                            setStyleSheet("border-image : url(Resources/assets/eggplant.png);")
                        continue
                if not a_plot["weed"]["no_weed"]:
                    self.get_cell_button(current_width, current_height). \
                        setStyleSheet("border-image : url(Resources/assets/weed.png);")

    def get_cell_button(self, width: int, height: int) -> QPushButton:
        return self.all_cells[width][height]

    def open_entity_window(self):
        sender = self.sender()
        print(f'{sender} was clicked!')
        self.window = QtWidgets.QDialog()
        self.ui = Ui_entity_screen()
        self.ui.setupUi(self.window, sender, self.controller)
        self.window.show()
        self.window.rejected.connect(self.fill_cells_with_images)

