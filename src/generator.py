import random
import src.attr as name_map
import flower as flower


def get_type():
    types = ["flower", "plume", "sands", "goblet", "ciclet"]
    return random.choices(types, k=1)[0]


if __name__ == "__main__":
    while True:
        type = get_type()
        if type == "flower":
            x = flower.flower_substats()
            for i in x:
                print(name_map.abbr[i[0]], round(i[1], 1))
            break
