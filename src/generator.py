import random
import src.flower as flower
import src.plume as plume
import src.sands as sands
import src.goblet as goblet
import src.circlet as circlet


def get_type():
    types = ["flower", "plume", "sands", "goblet", "ciclet"]
    return random.choices(types, k=1)[0]


def get_artifact():
    artifact_type = get_type()

    if artifact_type == "flower":
        x = flower.get_flower()
        return x
    elif artifact_type == "plume":
        x = plume.get_plume()
        return x
    elif artifact_type == "sands":
        x = sands.get_sands()
        return x
    elif artifact_type == "goblet":
        x = goblet.get_goblet()
        return x
    else:
        x = circlet.get_circlet()
        return x


