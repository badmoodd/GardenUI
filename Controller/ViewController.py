from Model.entities import *


class ViewController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self

    def rain_call(self):
        self.model.rain_call()
        self.model.write_entities_to("Resources/new_storage.json")

    def drought_call(self):
        self.model.drought_call()
        self.model.write_entities_to("Resources/new_storage.json")

    def watering_call(self, width, height):
        self.model.watering_call(width, height)
        self.model.write_entities_to("Resources/new_storage.json")

    def fertilizer_call(self, width, height):
        self.model.fertilizer_call(width, height)
        self.model.write_entities_to("Resources/new_storage.json")

    def weeding_call(self, width, height):
        self.model.weeding_call(width, height)
        self.model.write_entities_to("Resources/new_storage.json")

    def put_entity_to_cell(self, width, height, entity_name: str):
        print(entity_name)
        if entity_name == "Potato":
            self.model.set_plant(Potato(), width, height)
        if entity_name == "Carrot":
            self.model.set_plant(Carrot(), width, height)
        if entity_name == "Tomato":
            self.model.set_plant(Tomato(), width, height)
        if entity_name == "Cucumber":
            self.model.set_plant(Cucumber(), width, height)
        if entity_name == "Zucchini":
            self.model.set_plant(Zucchini(), width, height)
        if entity_name == "Eggplant":
            self.model.set_plant(Eggplant(), width, height)
        if entity_name == "Weed":
            self.model.set_weed(Weed(), width, height)
        if entity_name == "None":
            self.model.delete_plant(width, height)
            self.model.delete_weed(width, height)
        self.model.write_entities_to("Resources/new_storage.json")
