import random
import src.attr as name_map


"""Return artifact type"""
def get_type():
    types = ["flower", "plume", "sands", "goblet", "ciclet"]
    return random.choices(types, k=1)[0]


"""Return sub-stat"""
def get_substat():
    substats = ["atk", "def", "hpp", "atkp", "defp", "er", "em", "cr", "cd"]
    w = [14.45, 14.45, 10.8, 10.8, 10.8, 10.8, 10.8, 8.55, 8.55]
    return random.choices(substats, weights=w, k=1)[0]


"""Generate sub-stats for flower"""
def flower_substats():
    substats_count = random.choices([3, 4], [0.8, 0.2], k=1)[0]

    substats = []
    cnt = 0
    while cnt < substats_count:
        curr_substat = get_substat()
        if curr_substat not in substats:
            substats.append(curr_substat)
            cnt += 1
    return substats


if __name__ == "__main__":
    x = flower_substats()
    for i in x:
        print(name_map.abbr[i])
