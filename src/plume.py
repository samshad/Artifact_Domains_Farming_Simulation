import random
import src.substat_values as sv
import src.attr as name_map


def get_substat():
    substats = ["hp", "def", "hpp", "atkp", "defp", "er", "em", "cr", "cd"]
    w = [15.79, 15.79, 10.53, 10.53, 10.53, 10.53, 10.53, 7.89, 7.89]
    return random.choices(substats, weights=w, k=1)[0]


def get_plume():
    substats_count = random.choices([3, 4], [0.8, 0.2], k=1)[0]

    substats = []
    mainstat_value = 47
    cnt = 0
    already_got = []
    while cnt < substats_count:
        curr_substat = get_substat()
        if curr_substat not in already_got:
            val = sv.get_value(curr_substat)
            substats.append([name_map.abbr[curr_substat], val])
            already_got.append(curr_substat)
            cnt += 1
    return {
        "type": "Plume of Death",
        "mainstat": "ATK",
        "mainstat_value": mainstat_value,
        "substats": substats,
        "substats_count": substats_count,
        "level": 0
    }
