import random
import attr as name_map
import flower as flower
import plume as plume


def get_type():
    types = ["flower", "plume", "sands", "goblet", "ciclet"]
    return random.choices(types, k=1)[0]


if __name__ == "__main__":
    while True:
        artifact_type = get_type()
        if artifact_type == "flower":
            x = flower.get_flower()
            print(x)
            break
        elif artifact_type == "plume":
            x = plume.get_plume()
            print(x)
            break
