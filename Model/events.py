from Model.entities import Plant


class Events:
    @staticmethod
    def fertilizer_call(plant: Plant):
        if plant.health < 100:
            plant.health += 10
            if plant.health > 100:
                plant.health = 100
        if plant.size < 100:
            plant.size += 10
            if plant.size > 100:
                plant.size = 100
                plant.grownUp = True
