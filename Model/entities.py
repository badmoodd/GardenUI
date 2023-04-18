from abc import ABC, abstractmethod


class Plant:
    def __init__(self, size, health, fruits_count, grown_up, is_thirsty):
        self.size = size
        self.health = health
        self.fruits_count = fruits_count
        self.grown_up = grown_up
        self.is_thirsty = is_thirsty

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def give_fruits(self):
        pass

    def is_grown_up(self):
        return self.grown_up

    def get_size(self):
        return self.size

    def get_health(self):
        return self.health

    def get_fruits_count(self):
        return self.fruits_count

    def set_fruits_count(self, fruits_count):
        self.fruits_count = fruits_count


class Vegetable(Plant, ABC):
    def __init__(self, size, health, fruits_count, grown_up, is_thirsty):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def grow(self):
        if self.size < 100:
            self.size += 25
        if self.size == 100:
            self.grown_up = True


class Potato(Vegetable):
    def __init__(self, size=20, health=50, fruits_count=0, grown_up=False, is_thirsty=False):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def give_fruits(self):
        if self.grown_up:
            self.fruits_count += 3


class Carrot(Vegetable):
    def __init__(self, size=20, health=50, fruits_count=0, grown_up=False, is_thirsty=False):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def give_fruits(self):
        if self.grown_up:
            self.fruits_count += 1


class Tomato(Vegetable):
    def __init__(self, size=20, health=50, fruits_count=0, grown_up=False, is_thirsty=False):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def give_fruits(self):
        if self.grown_up:
            self.fruits_count += 5


class Cucumber(Vegetable):
    def __init__(self, size=20, health=50, fruits_count=0, grown_up=False, is_thirsty=False):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def give_fruits(self):
        if self.grown_up:
            self.fruits_count += 5


class Eggplant(Vegetable):
    def __init__(self, size=20, health=50, fruits_count=0, grown_up=False, is_thirsty=False):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def give_fruits(self):
        if self.grown_up:
            self.fruits_count += 5


class Zucchini(Vegetable):
    def __init__(self, size=20, health=50, fruits_count=0, grown_up=False, is_thirsty=False):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def give_fruits(self):
        if self.grown_up:
            self.fruits_count += 3


class Weed:
    def __init__(self):
        self.damage = 10

    def damage_plant(self, plant):
        plant.health -= self.damage
