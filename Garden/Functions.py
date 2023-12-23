import sys
import getopt
import random
from Model.entities import *
from Model.garden import Garden

PATH_TO_PLANTS = "Resources/new_storage.json"


def init_garden():
    data_dict = {}
    width = None
    height = None
    set_pl = None
    set_os = None
    pl_to_del = None
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "g:w:h:s:o:d:f:t:i:rq", ["garden= ",
                                                                  "width=",
                                                                  "height=",
                                                                  "setPlant=",
                                                                  "setOsot=",
                                                                  "delPlant=",
                                                                  "rain=",
                                                                  "drought=",
                                                                  "fertilizer=",
                                                                  "watering=",
                                                                  "weeding="])

    except:
        print("Error")

    for opt, arg in opts:
        if opt in ['-w', '--width']:
            width = arg
            data_dict['width'] = int(width)
        if opt in ['-h', '--height']:
            height = arg
            data_dict['height'] = int(height)
        if opt in ['-s', '--setPlant']:
            set_pl = arg
            lst = arg.split()
            entity = what_plant(lst)
            # garden_size_dict = read_garden_size(PATH_TO_PLANTS)
            garden = Garden()
            garden.read_entities_from(PATH_TO_PLANTS)
            garden.set_plant(entity, int(lst[1]), int(lst[2]))
            garden.write_entities_to(PATH_TO_PLANTS)
            data_dict['plant'] = set_pl
        if opt in ['-o', '--setOsot']:
            set_os = arg
            lst = arg.split()
            # garden_size_dict = read_garden_size(PATH_TO_PLANTS)
            garden = Garden()
            garden.read_entities_from(PATH_TO_PLANTS)
            garden.set_weed(Weed(), int(lst[0]), int(lst[1]))
            garden.write_entities_to(PATH_TO_PLANTS)
            data_dict['osot'] = set_os
        if opt in ['-d', '--delPlant']:
            pl_to_del = arg
            lst = arg.split()
            # garden_size_dict = read_garden_size(PATH_TO_PLANTS)
            garden = Garden()
            garden.read_entities_from(PATH_TO_PLANTS)
            garden.delete_plant(int(lst[0]), int(lst[1]))
            garden.write_entities_to(PATH_TO_PLANTS)
            data_dict['pl_to_del'] = pl_to_del
        if opt in ['-r', '--rain']:
            # garden_size_dict = read_garden_size(PATH_TO_PLANTS)
            garden = Garden()
            garden.read_entities_from(PATH_TO_PLANTS)
            garden.rain_call()
            ran_width = random.randint(0, garden.width - 1)
            ran_height = random.randint(0, garden.height - 1)
            garden.set_weed(Weed(), ran_width, ran_height)
            garden.write_entities_to(PATH_TO_PLANTS)
            data_dict['is_rain'] = True
        if opt in ['-q', '--drought']:
            # garden_size_dict = read_garden_size(PATH_TO_PLANTS)
            garden = Garden()
            garden.read_entities_from(PATH_TO_PLANTS)
            garden.drought_call()
            garden.write_entities_to(PATH_TO_PLANTS)
            data_dict['is_drought'] = True
        if opt in ['-f', '--fertilizer']:
            lst = arg.split()
            # garden_size_dict = read_garden_size(PATH_TO_PLANTS)
            garden = Garden()
            garden.read_entities_from(PATH_TO_PLANTS)
            garden.fertilizer_call(int(lst[0]), int(lst[1]))
            garden.write_entities_to(PATH_TO_PLANTS)
            data_dict['fertilizer'] = arg
        if opt in ['-t', '--watering']:
            lst = arg.split()
            # garden_size_dict = read_garden_size(PATH_TO_PLANTS)
            garden = Garden()
            garden.read_entities_from(PATH_TO_PLANTS)
            garden.watering_call(int(lst[0]), int(lst[1]))
            garden.write_entities_to(PATH_TO_PLANTS)
            data_dict['watering'] = arg
        if opt in ['-i', '--weeding']:
            lst = arg.split()
            # garden_size_dict = read_garden_size(PATH_TO_PLANTS)
            garden = Garden()
            garden.read_entities_from(PATH_TO_PLANTS)
            garden.weeding_call(int(lst[0]), int(lst[1]))
            garden.write_entities_to(PATH_TO_PLANTS)
            data_dict['weeding'] = arg
        if opt in ['-g', '--garden']:
            lst = arg.split(' ')
            data_dict['garden'] = lst
            garden = Garden()
            garden.write_entities_to(PATH_TO_PLANTS)

    print(data_dict)
    return data_dict


def what_plant(lst):
    if lst[0] == "carrot":
        return Carrot()
    if lst[0] == "tomato":
        return Tomato()
    if lst[0] == "potato":
        return Potato()
    if lst[0] == "cucumber":
        return Cucumber()
    if lst[0] == "zucchini":
        return Zucchini()
    if lst[0] == "eggplant":
        return Eggplant()

    # if lst[0] == "apple_tree":
    #     return AppleTree()
    # if lst[0] == "plum_tree":
    #     return PlumTree()
    # if lst[0] == "pear_tree":
    #     return PearTree()


# def read_garden_size(path_to_file):
#     with open(path_to_file, 'r') as file:
#         new_dict = json.load(file)
#         return new_dict
