import json
from Model.entities import *


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Plot:
    def __init__(self, plant=None, weed=None):
        self.plant = plant
        self.weed = weed
        self.is_empty = True

        if self.plant is not None:
            self.is_empty = False

        if self.weed is not None:
            self.is_empty = False


class Garden:
    def __init__(self):
        self.width = 4
        self.height = 5
        self.arr_plot = [[Plot() for j in range(self.height)] for i in range(self.width)]

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

    def rain_call(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.arr_plot[i][j].is_empty or self.arr_plot[i][j].plant is None:
                    continue
                self.watering_call(i, j)

    #    чутка модил
    def drought_call(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.arr_plot[self.width][self.height].is_empty or self.arr_plot[self.width][self.height].plant is None:
                    continue
                if self.arr_plot[self.width][self.height].plant.is_thirsty:
                    self.arr_plot[self.width][self.height].plant.health -= 15
                else:
                    self.arr_plot[self.width][self.height].plant.is_thirsty = True

    def set_plant(self, plant, width, height):
        plot = Plot()
        if self.arr_plot[width][height].weed is not None:
            plot.weed = self.arr_plot[width][height].weed
        plot.plant = plant
        self.arr_plot[width][height] = plot
        self.arr_plot[width][height].is_empty = False

    def set_weed(self, weed, width, height):
        self.arr_plot[width][height].weed = weed
        self.arr_plot[width][height].is_empty = False

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
        if self.arr_plot[width][height].weed is None:
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
                weed_dict = {}
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
                        if isinstance(self.arr_plot[i][j].plant, Cucumber):
                            plant_dict['name_of_plant'] = "cucumber"
                        if isinstance(self.arr_plot[i][j].plant, Zucchini):
                            plant_dict['name_of_plant'] = "zucchini"
                        if isinstance(self.arr_plot[i][j].plant, Eggplant):
                            plant_dict['name_of_plant'] = "eggplant"
                        plant_dict['fruits_count'] = self.arr_plot[i][j].plant.fruits_count
                        plant_dict['grown_up'] = self.arr_plot[i][j].plant.grown_up
                        plant_dict['health'] = self.arr_plot[i][j].plant.health
                        plant_dict['is_thirsty'] = self.arr_plot[i][j].plant.is_thirsty
                        plant_dict['size'] = self.arr_plot[i][j].plant.size
                        plant_dict['no_plant'] = False
                    if self.arr_plot[i][j].plant is None:
                        plant_dict['no_plant'] = True
                    if self.arr_plot[i][j].weed is not None:
                        weed_dict['damage'] = 10
                        weed_dict['no_weed'] = False
                    if self.arr_plot[i][j].weed is None:
                        weed_dict['no_weed'] = True
                plot_dict['plant'] = plant_dict
                plot_dict['weed'] = weed_dict
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
                    if item['plant']['name_of_plant'] == 'cucumber':
                        self.set_plant(Cucumber(item['plant']['size'], item['plant']['health'],
                                                item['plant']['fruits_count'], item['plant']['grown_up'],
                                                item['plant']['is_thirsty']), item['width'], item['height'])
                    if item['plant']['name_of_plant'] == 'zucchini':
                        self.set_plant(Zucchini(item['plant']['size'], item['plant']['health'],
                                                item['plant']['fruits_count'], item['plant']['grown_up'],
                                                item['plant']['is_thirsty']), item['width'], item['height'])
                    if item['plant']['name_of_plant'] == 'eggplant':
                        self.set_plant(Eggplant(item['plant']['size'], item['plant']['health'],
                                                item['plant']['fruits_count'], item['plant']['grown_up'],
                                                item['plant']['is_thirsty']), item['width'], item['height'])
                if not item['weed']['no_weed']:
                    self.set_weed(Weed(), item['width'], item['height'])
