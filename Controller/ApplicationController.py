import json


class ApplicationController:

    @staticmethod
    def read_entities_from(path_to_file) -> dict:
        with open(path_to_file, 'r') as file:
            entities: dict = json.load(file)
        return entities
