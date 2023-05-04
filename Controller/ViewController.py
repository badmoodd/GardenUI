from Model.garden import Garden


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
