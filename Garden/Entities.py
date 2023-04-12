import json
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


class Tree(Plant, ABC):
    def __init__(self, size, health, fruits_count, grown_up, is_thirsty):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def grow(self):
        if self.size < 100:
            self.size += 20
        if self.size == 100:
            self.grown_up = True


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


class AppleTree(Tree):
    def __init__(self, size=20, health=50, fruits_count=0, grown_up=False, is_thirsty=False):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def give_fruits(self):
        if self.grown_up:
            self.fruits_count += 15


class PearTree(Tree):
    def __init__(self, size=20, health=50, fruits_count=0, grown_up=False, is_thirsty=False):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def give_fruits(self):
        if self.grown_up:
            self.fruits_count += 15


class PlumTree(Tree):
    def __init__(self, size=20, health=50, fruits_count=0, grown_up=False, is_thirsty=False):
        super().__init__(size, health, fruits_count, grown_up, is_thirsty)

    def give_fruits(self):
        if self.grown_up:
            self.fruits_count += 15


class Events:
    @staticmethod
    def fertilizer_call(plant):
        if plant.health < 100:
            plant.health += 10
            if plant.health > 100:
                plant.health = 100
        if plant.size < 100:
            plant.size += 10
            if plant.size > 100:
                plant.size = 100
                plant.grownUp = True

    @staticmethod
    def cells_around(width, height, arr_width, arr_height):
        pair_array_list = []
        if width - 1 >= 0:
            pair_array_list.append((width - 1, height))
            if height - 1 >= 0:
                pair_array_list.append((width - 1, height - 1))
            if height + 1 <= arr_height - 1:
                pair_array_list.append((width - 1, height + 1))
        if width + 1 <= arr_width - 1:
            pair_array_list.append((width + 1, height))
            if height - 1 >= 0:
                pair_array_list.append((width + 1, height - 1))
            if height + 1 <= arr_height - 1:
                pair_array_list.append((width + 1, height + 1))
        if height - 1 >= 0:
            pair_array_list.append((width, height - 1))
        if height + 1 <= arr_height - 1:
            pair_array_list.append((width, height + 1))
        pair_array_list.append((width, height))
        return pair_array_list


class Osot:
    def __init__(self):
        self.damage = 10

    def damage_plant(self, plant):
        plant.health -= self.damage


class Plot:
    def __init__(self, plant=None, osot=None):
        self.plant = plant
        self.osot = osot
        self.is_empty = True

        if self.plant is not None:
            self.is_empty = False

        if self.osot is not None:
            self.is_empty = False


class Garden:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.arr_plot = [[Plot() for j in range(height)] for i in range(width)]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def rain_call(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.arr_plot[i][j].is_empty or self.arr_plot[i][j].plant is None:
                    continue
                self.watering_call(i, j)

    def drought_call(self):
        for i in self.arr_plot:
            for plot in i:
                if plot.is_empty or plot.plant is None:
                    continue
                if plot.plant.is_thirsty:
                    plot.plant.health -= 15
                else:
                    plot.plant.is_thirsty = True

    def set_plant(self, plant, width, height):
        plot = Plot()
        if self.arr_plot[width][height].osot is not None:
            plot.osot = self.arr_plot[width][height].osot
        plot.plant = plant
        self.arr_plot[width][height] = plot
        self.arr_plot[width][height].is_empty = False

    def set_osot(self, osot, width, height):
        self.arr_plot[width][height].osot = osot
        self.arr_plot[width][height].is_empty = False

    def watering_call(self, width, height):
        if self.arr_plot[width][height].plant is not None:

            if self.arr_plot[width][height].plant.is_thirsty:
                self.arr_plot[width][height].plant.health += 10
                if self.arr_plot[width][height].plant.health > 100:
                    self.arr_plot[width][height].plant.health = 100
            if self.arr_plot[width][height].plant.size < 100:
                self.arr_plot[width][height].plant.size += 10
                if self.arr_plot[width][height].plant.size > 100:
                    self.arr_plot[width][height].plant.size = 100
                    self.arr_plot[width][height].plant.grown_up = True
            self.arr_plot[width][height].plant.is_thirsty = False

    def weeding_call(self, width, height):
        array_of_cells_around = Events.cells_around(width, height, len(self.arr_plot), len(self.arr_plot[0]))
        for pair in array_of_cells_around:
            self.arr_plot[pair[0]][pair[1]].osot = None
            if self.arr_plot[pair[0]][pair[1]].plant is None:
                self.arr_plot[pair[0]][pair[1]].is_empty = True

    def fertilizer_call(self, width, height):
        if self.arr_plot[width][height].plant is not None:
            if self.arr_plot[width][height].plant.health < 100:
                self.arr_plot[width][height].plant.health += 10
                if self.arr_plot[width][height].plant.health > 100:
                    self.arr_plot[width][height].plant.health = 100
            if self.arr_plot[width][height].plant.size < 100:
                self.arr_plot[width][height].plant.size += 10
                if self.arr_plot[width][height].plant.size >= 100:
                    self.arr_plot[width][height].plant.size = 100
                    self.arr_plot[width][height].plant.grown_up = True

    def delete_plant(self, width, height):
        self.arr_plot[width][height].plant = None
        if self.arr_plot[width][height].osot is None:
            self.arr_plot[width][height].is_empty = True

    def read_entities_from(self, path_to_file):
        with open(path_to_file, 'r') as file:
            new_dict = json.load(file)
        self.filling_list_of_entities(new_dict)

    def write_entities_to(self, path_to_file):
        with open(path_to_file, 'w') as file:
            json.dump(self.filling_list_as_dict(), file, indent=3)

    def filling_list_as_dict(self):
        new_dict = {}
        new_list_of_plots = []

        for i in range(self.width):
            for j in range(self.height):
                plot_dict = {}
                plant_dict = {}
                osot_dict = {}
                plot_dict['width'] = i
                plot_dict['height'] = j
                plot_dict['is_empty'] = self.arr_plot[i][j].is_empty
                if self.arr_plot[i][j].is_empty:
                    new_list_of_plots.append(plot_dict)
                    continue
                else:
                    if self.arr_plot[i][j].plant is not None:
                        if isinstance(self.arr_plot[i][j].plant, Potato):
                            plant_dict['name_of_plant'] = "potato"
                        if isinstance(self.arr_plot[i][j].plant, Carrot):
                            plant_dict['name_of_plant'] = "carrot"
                        if isinstance(self.arr_plot[i][j].plant, Tomato):
                            plant_dict['name_of_plant'] = "tomato"
                        if isinstance(self.arr_plot[i][j].plant, AppleTree):
                            plant_dict['name_of_plant'] = "apple_tree"
                        if isinstance(self.arr_plot[i][j].plant, PearTree):
                            plant_dict['name_of_plant'] = "pear_tree"
                        if isinstance(self.arr_plot[i][j].plant, PlumTree):
                            plant_dict['name_of_plant'] = "plum_tree"
                        plant_dict['fruits_count'] = self.arr_plot[i][j].plant.fruits_count
                        plant_dict['grown_up'] = self.arr_plot[i][j].plant.grown_up
                        plant_dict['health'] = self.arr_plot[i][j].plant.health
                        plant_dict['is_thirsty'] = self.arr_plot[i][j].plant.is_thirsty
                        plant_dict['size'] = self.arr_plot[i][j].plant.size
                        plant_dict['no_plant'] = False
                    if self.arr_plot[i][j].plant is None:
                        plant_dict['no_plant'] = True
                    if self.arr_plot[i][j].osot is not None:
                        osot_dict['damage'] = 10
                        osot_dict['no_osot'] = False
                    if self.arr_plot[i][j].osot is None:
                        osot_dict['no_osot'] = True
                plot_dict['plant'] = plant_dict
                plot_dict['osot'] = osot_dict
                new_list_of_plots.append(plot_dict)
        new_dict['garden_width'] = self.width
        new_dict['garden_height'] = self.height
        new_dict['plots'] = new_list_of_plots
        return new_dict

    def filling_list_of_entities(self, load_dict):
        self.width = load_dict['garden_width']
        self.height = load_dict['garden_height']
        for item in load_dict['plots']:
            if item['is_empty']:
                continue
            else:
                if not item['plant']['no_plant']:
                    if item['plant']['name_of_plant'] == 'potato':
                        self.set_plant(Potato(item['plant']['size'], item['plant']['health'],
                                              item['plant']['fruits_count'], item['plant']['grown_up'],
                                              item['plant']['is_thirsty']), item['width'], item['height'])
                    if item['plant']['name_of_plant'] == 'carrot':
                        self.set_plant(Carrot(item['plant']['size'], item['plant']['health'],
                                              item['plant']['fruits_count'], item['plant']['grown_up'],
                                              item['plant']['is_thirsty']), item['width'], item['height'])
                    if item['plant']['name_of_plant'] == 'tomato':
                        self.set_plant(Tomato(item['plant']['size'], item['plant']['health'],
                                              item['plant']['fruits_count'], item['plant']['grown_up'],
                                              item['plant']['is_thirsty']), item['width'], item['height'])
                    if item['plant']['name_of_plant'] == 'apple_tree':
                        self.set_plant(AppleTree(item['plant']['size'], item['plant']['health'],
                                                 item['plant']['fruits_count'], item['plant']['grown_up'],
                                                 item['plant']['is_thirsty']), item['width'], item['height'])
                    if item['plant']['name_of_plant'] == 'plum_tree':
                        self.set_plant(PlumTree(item['plant']['size'], item['plant']['health'],
                                                item['plant']['fruits_count'], item['plant']['grown_up'],
                                                item['plant']['is_thirsty']), item['width'], item['height'])
                    if item['plant']['name_of_plant'] == 'pear_tree':
                        self.set_plant(PearTree(item['plant']['size'], item['plant']['health'],
                                                item['plant']['fruits_count'], item['plant']['grown_up'],
                                                item['plant']['is_thirsty']), item['width'], item['height'])
                if not item['osot']['no_osot']:
                    self.set_osot(Osot(), item['width'], item['height'])


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
